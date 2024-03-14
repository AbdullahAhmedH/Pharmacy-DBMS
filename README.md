# Pharmacy Management System

## Description
This repository contains the code for a web-based Pharmacy Management System. The system allows users to manage various aspects of a pharmacy, including notifications, doctors, patients, suppliers, medicines, batches, prescriptions, and billing.

## Features
- **Notifications Management:** Users can view, add, and mark notifications as completed.
- **Doctors Management:** Users can add, view, and delete doctor information, including their name, contact details, work address, and specialty.
- **Patients Management:** Users can add, view, and delete patient information, including their name, contact details, address, and gender.
- **Suppliers Management:** Users can add, view, and delete supplier information, including their name and location.
- **Medicines Management:** Users can add, view, and delete medicine information, including its name, company, cost per unit, type, and over-the-counter (OTC) status.
- **Batches Management:** Users can add, view, and delete batches of medicines, including information such as batch ID, timestamp, supplier ID, medicine ID, quantity, and expiry date.
- **Prescriptions Management:** Users can check patient IDs and bill prescriptions, including essential medicines and over-the-counter medicines. Prescription details include medicine ID, quantity, and cost.
- **Billing:** Users can calculate and mark bills as paid, including essential medicines and over-the-counter medicines. The system checks batch availability and expiry dates before marking the bill as paid.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript, AngularJS
- **Backend:** Python (Flask)
- **Database:** MySQL

## Installation

### Backend
1. Navigate to the `backend` folder in your terminal.
2. Activate the virtual environment:
    - On Windows:
    ```bash
    .venv\Scripts\activate.ps1
    ```
    or open the terminal in .venv\Scripts and:
    ```bash
    ./activate.ps1
    ```
    - On macOS and Linux:
    ```bash
    source .venv/bin/activate
    ```
3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Open `app.py` and update the database connection settings (e.g., host, username, password) to match your MySQL database credentials.
5. Run the Flask application by moving to backend folder and type:
    ```bash
    flask run
    ```

### MySQL Database
1. Import the `pharmacy.sql` file into your MySQL database to set up the database schema:
    ```bash
    mysql -u username -p pharmacy < pharmacy.sql
    ```
   Replace `username` with your MySQL username.

### Running the Application
1. Ensure your MySQL server is running.
2. With both the backend and frontend components set up, you can access the Pharmacy Management System by opening a web browser and navigating to the appropriate URL, typically `http://localhost:port`, where `port` is the port number on which your Flask server is running (default is usually 5000).


