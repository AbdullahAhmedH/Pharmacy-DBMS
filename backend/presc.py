import mysql.connector


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='pharmacy'
        )

        if connection.is_connected():
            print('Connected to MySQL database')
            return connection

    except mysql.connector.Error as e:
        print(f'Error connecting to MySQL database: {e}')
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print('Connection closed')

def add_prescription(connection):
    try:
        cursor = connection.cursor()

        patient_id = int(input("Enter patient ID: "))
        doc_id = int(input("Enter doctor ID: "))
        paid = "N"
        cursor.execute("SELECT MAX(Presc_id) FROM prescription")
        presc_id = cursor.fetchall()[0][0]
        if presc_id is None:
            presc_id = 1
        else:
            presc_id = int(presc_id) + 1
        cursor.execute("INSERT INTO prescription VALUES (%s, %s, %s, %s)",
                       (presc_id, patient_id, doc_id, paid))
        connection.commit()
        print("Here's a list of medicines:")
        cursor.execute("SELECT Med_id, Med_name, Med_cost_unit FROM medicine")
        medicines = cursor.fetchall()
        for med_id, med_name, med_cost_unit in medicines:
            print(f"{med_id}: {med_name} - Unit Cost: {med_cost_unit}")

        print("If you'd like to add a medicine, enter its id. if you're done adding, enter 0")
        while True:
            med_id_input = input()
            if med_id_input == '0':
                break
            else:
                med_id = int(med_id_input)
                med_qty = int(input(f"Enter quantity for medicine with ID {med_id}: "))
                cursor.execute("SELECT Med_cost_unit FROM medicine WHERE Med_id = %s", (med_id,))
                med_cost_unit = cursor.fetchone()[0]
                cost = med_qty * med_cost_unit
                cursor.execute("INSERT INTO presc_details VALUES (%s, %s, %s, %s)",
                               (presc_id, med_id, med_qty, cost))
                connection.commit()
                print("Medicine added to prescription.")

    except mysql.connector.Error as e:
        print(f'Error adding prescription: {e}')

def delete_prescription(connection):
    try:
        cursor = connection.cursor()

        presc_id = int(input("Enter prescription ID to delete: "))
        cursor.execute("DELETE FROM presc_details WHERE Presc_id = %s", (presc_id,))
        cursor.execute("DELETE FROM prescription WHERE Presc_id = %s", (presc_id,))
        connection.commit()

        print("Prescription deleted successfully")

    except mysql.connector.Error as e:
        print(f'Error deleting prescription: {e}')

def view_prescriptions(connection):
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM prescription")
        prescriptions = cursor.fetchall()

        print("Prescriptions:")
        for prescription in prescriptions:
            print(prescription)

    except mysql.connector.Error as e:
        print(f'Error viewing prescriptions: {e}')

def main():
    connection = connect_to_database()
    if not connection:
        return

    while True:
        print("\n0-Exit\n1-Add Prescription\n2-Delete Prescription\n3-View Prescription")
        choice = int(input("Enter choice: "))

        if choice == 0:
            break
        elif choice == 1:
            add_prescription(connection)
        elif choice == 2:
            delete_prescription(connection)
        elif choice == 3:
            view_prescriptions(connection)
        else:
            print("Invalid choice")

    close_connection(connection)

if __name__ == "__main__":
    main()
