from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_mysqldb import MySQL

app = Flask(__name__,static_folder='../frontend')

#SQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'your_mysql_database'

# Dummy database of users (replace with a real database)
users = {
    'user1': 'password1',
    'user2': 'password2'
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
        return send_from_directory('../frontend', 'login.html')

# Redirect users to the login page when they access the root URL
@app.route('/')
def index():
    return redirect(url_for('login'))

# Protected area of the application
@app.route('/content')
def content():
    # This route represents the content page accessible after successful login
    return send_from_directory('../frontend', 'content.html')

if __name__ == '__main__':
    app.run(debug=True)
