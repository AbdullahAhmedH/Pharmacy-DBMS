from flask import (Flask, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'pharmacy'

# Initialize MySQL
mysql = MySQL(app)

# Dummy database of users (replace with a real database)
users = {
    'u1': 'pwd1',
    'u2': 'pwd2'
}

# Define route to serve the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists and password matches
        if username in users and users[username] == password:
            # Authentication successful, redirect to the content page
            return redirect(url_for('content'))
        else:
            # Authentication failed, redirect back to the login page with an error message
            return render_template('login.html', error='Invalid username or password')
    else:
        # If it's a GET request, render the login page
        return render_template('login.html')

# Redirect users to the login page when they access the root URL
@app.route('/')
def index():
    return redirect(url_for('login'))

# Protected area of the application
@app.route('/content')
def content():
    # This route represents the content page accessible after successful login
    return send_from_directory('../frontend', 'content.html')

# Logout route
@app.route('/logout')
def logout():
    # Redirect to the login page
    return redirect(url_for('login'))

# Endpoint to fetch notifications data
@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    # Fetch notifications data from database (replace this with your database query)
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM notifs WHERE priority >=1")
    notifications = cursor.fetchall()
    return jsonify(notifications)

# Endpoint to add a new notification
@app.route('/api/add_notification', methods=['POST'])
def add_notification():
    # Receive new notification data from the request
    new_notification = request.json
    
    # Insert new notification into database (replace this with your database insert operation)
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT MAX(Notif_id) FROM notifs")
    next_sno = cursor.fetchall()[0][0];
    if next_sno is None:
        next_sno = 1
    else:
        next_sno+=1
    cursor.execute("INSERT INTO notifs VALUES (%s, %s, %s)", (next_sno, new_notification['priority'], new_notification['detail']))
    mysql.connection.commit()
    response = {'message': 'Notification added successfully'}
    return jsonify(response)

# Endpoint to mark a notification as completed
@app.route('/api/mark_as_completed', methods=['POST'])
def mark_as_completed():
    # Receive notification ID from the request
    notification_id = request.json['notificationId']
    
    # Mark the notification as completed in the database
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE notifs SET Priority = 0 WHERE Notif_id = %s", (notification_id,))
    mysql.connection.commit()
    response = {'message': 'Notification marked as completed successfully'}
    return jsonify(response)

@app.route('/api/doctor', methods=['GET'])
def get_doctors():
    # Fetch doctors data from database (replace this with your database query)
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    return jsonify(doctors)

@app.route('/api/add_doctor', methods=['POST'])
def add_doctor():
    new_doctor = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT doc_id FROM doctor")
    doc_ids = [res[0] for res in cursor.fetchall()]
    print(new_doctor,doc_ids)
    if int(new_doctor['doc_id']) in doc_ids:
        response = {'message': 'Doctor with ID already exists'}
        return jsonify(response)
    else:
        cursor.execute("INSERT INTO doctor VALUES (%s, %s, %s, %s, %s)", (new_doctor['doc_id'],new_doctor['doc_name'], new_doctor['doc_mobile'], new_doctor['doc_work_address'], new_doctor['doc_speciality']))
        mysql.connection.commit()
        response = {'message': 'Doctor added successfully'}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
