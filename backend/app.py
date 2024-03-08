from datetime import datetime

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
    if int(new_doctor['doc_id']) in doc_ids:
        response = {'message': 'Doctor with ID already exists'}
        return jsonify(response)
    else:
        cursor.execute("INSERT INTO doctor VALUES (%s, %s, %s, %s, %s)", (new_doctor['doc_id'],new_doctor['doc_name'], new_doctor['doc_mobile'], new_doctor['doc_work_address'], new_doctor['doc_speciality']))
        mysql.connection.commit()
        response = {'message': 'Doctor added successfully'}
        return jsonify(response)

@app.route('/api/delete_doctor/', methods=['POST'])
def delete_doctor():
    doc_id = request.json['doc_id']
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM doctor WHERE doc_id = %s", (doc_id,))
        mysql.connection.commit()
        response = {'message': 'Doctor information deleted successfully'}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/api/patient', methods=['GET'])
def get_patients():
    # Fetch patients data from database (replace this with your database query)
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    return jsonify(patients)

@app.route('/api/add_patient', methods=['POST'])
def add_patient():
    new_patient = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Patient_id FROM patient")
    patient_ids = [res[0] for res in cursor.fetchall()]
    print(patient_ids,new_patient)
    if int(new_patient['patient_id']) in patient_ids:
        response = {'message': 'Patient with ID already exists'}
        return jsonify(response)
    else:
        cursor.execute("INSERT INTO patient (Patient_id, Patient_name, patient_mobile, Patient_address, Sex) VALUES (%s, %s, %s, %s, %s)", 
                       (new_patient['patient_id'], new_patient['patient_name'], new_patient['patient_mobile'], new_patient['patient_address'], new_patient['sex']))
        mysql.connection.commit()
        response = {'message': 'Patient added successfully'}
        return jsonify(response)

@app.route('/api/delete_patient/', methods=['POST'])
def delete_patient():
    print(request.json)
    patient_id = request.json['patient_id']
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM patient WHERE Patient_id = %s", (patient_id,))
        mysql.connection.commit()
        response = {'message': 'Patient information deleted successfully'}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/api/suppliers', methods=['GET'])
def get_suppliers():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM supplier")
    suppliers = cursor.fetchall()
    return jsonify(suppliers)

@app.route('/api/add_supplier', methods=['POST'])
def add_supplier():
    new_supplier = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT supplier_id FROM supplier")
    supplier_ids = [res[0] for res in cursor.fetchall()]
    if int(new_supplier['supplier_id']) in supplier_ids:
        response = {'message': 'Supplier with ID already exists'}
        return jsonify(response)
    else:
        cursor.execute("INSERT INTO supplier VALUES (%s, %s, %s)", (new_supplier['supplier_id'], new_supplier['supplier_name'], new_supplier['supplier_location']))
        mysql.connection.commit()
        response = {'message': 'Supplier added successfully'}
        return jsonify(response)

@app.route('/api/delete_supplier/', methods=['POST'])
def delete_supplier():
    supplier_id = request.json['supplier_id']
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM supplier WHERE supplier_id = %s", (supplier_id,))
        mysql.connection.commit()
        response = {'message': 'Supplier information deleted successfully'}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/api/medicines', methods=['GET'])
def get_medicines():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM medicine")
    medicines = cursor.fetchall()
    return jsonify(medicines)

@app.route('/api/add_medicine', methods=['POST'])
def add_medicine():
    new_medicine = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT Med_id FROM medicine")
    medicine_ids = [res[0] for res in cursor.fetchall()]
    if int(new_medicine['Med_id']) in medicine_ids:
        response = {'message': 'Medicine with ID already exists'}
        return jsonify(response)
    else:
        cursor.execute("INSERT INTO medicine VALUES (%s, %s, %s, %s, %s, %s)", (new_medicine['Med_id'], new_medicine['Med_name'], new_medicine['Med_company'], new_medicine['Med_cost_unit'], new_medicine['Med_type'], new_medicine['Is_OTC']))
        mysql.connection.commit()
        response = {'message': 'Medicine added successfully'}
        return jsonify(response)

@app.route('/api/delete_medicine/', methods=['POST'])
def delete_medicine():
    med_id = request.json['Med_id']
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM medicine WHERE Med_id = %s", (med_id,))
        mysql.connection.commit()
        response = {'message': 'Medicine information deleted successfully'}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/api/batches', methods=['GET'])
def get_batches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM batch")
    batches = cursor.fetchall()
    transformed_batches = []
    for batch in batches:
        transformed_batch = {
            'Batch_id': batch[0],
            'Batch_timestamp': batch[1].strftime('%Y-%m-%d'),  # Assuming Batch_timestamp is a datetime object
            'Supplier_id': batch[2],
            'Med_id': batch[3],
            'Batch_qty': batch[4],
            'Batch_expiry': batch[5].strftime('%Y-%m-%d')  # Assuming Batch_expiry is a date object
        }
        transformed_batches.append(transformed_batch)
    return jsonify(transformed_batches)

@app.route('/api/add_batch', methods=['POST'])
def add_batch():
    new_batch = request.json
    cursor = mysql.connection.cursor()
    batch_expiry = datetime.fromisoformat(new_batch['Batch_expiry']).date()
    cursor.execute("INSERT INTO batch (Batch_id, Batch_timestamp, Supplier_id, Med_id, Batch_qty, Batch_expiry) VALUES (%s, NOW(), %s, %s, %s, %s)",
                   (new_batch['Batch_id'], new_batch['Supplier_id'], new_batch['Med_id'], new_batch['Batch_qty'], batch_expiry))
    mysql.connection.commit()
    response = {'message': 'Batch added successfully'}
    return jsonify(response)

@app.route('/api/delete_batch/', methods=['POST'])
def delete_batch():
    batch_id = request.json['Batch_id']
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM batch WHERE Batch_id = %s", (batch_id,))
        mysql.connection.commit()
        response = {'message': 'Batch information deleted successfully'}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/api/patient_id_presc', methods=['GET'])
def check_patient_id_presc():
    patient_id = request.args.get('patientId')

    if patient_id is None:
        return jsonify({'error': 'Patient ID not provided'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM prescription WHERE Patient_id = %s AND paid == N", (patient_id,))
    presc = cursor.fetchall()
    if presc:
        return jsonify(presc), 200
    else:
        return jsonify({'message': 'Prescription not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
