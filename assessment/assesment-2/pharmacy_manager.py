import mysql.connector

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Manager(User):
    def __init__(self, user_id, name, pharmacy_name):
        super().__init__(user_id, name)
        self.pharmacy_name = pharmacy_name


class PharmacyManager(Manager):
    def __init__(self, db_connector):
        super().__init__(None, None, None)
        self.db_connector = db_connector

    def register(self):
        name = input("Enter name: ")
        pharmacy_name = input("Enter pharmacy name: ")

        connection = self.db_connector.connect()

        query = "INSERT INTO managers (name, pharmacy_name) VALUES (%s, %s)"
        values = (name, pharmacy_name)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        print("Manager registered successfully.")

    def login(self):
        name = input("Enter name: ")
        pharmacy_name = input("Enter pharmacy name: ")
       
        connection = self.db_connector.connect()

        query = "SELECT * FROM managers WHERE name = %s AND pharmacy_name = %s"
        values = (name, pharmacy_name)
        cursor = connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            print("Manager login successful.")
        else:
            print("Invalid credentials.")

    def add_medicine(self):
        connection = self.db_connector.connect()

        query = "INSERT INTO medicines (name, quantity, added_date, added_by, price) VALUES (%s, %s, %s, %s, %s)"
        values = (name, quantity, added_date, added_by, price)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        print("Medicine added successfully.")

    def view_medicines(self):

        connection = self.db_connector.connect()

        query = "SELECT * FROM medicines"
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        print("Medicines:")
        for result in results:
            print(result)

    def delete_medicine(self):
        # Implement logic to delete a specific medicine

        # Prompt the user for input values

        # Validate input values

        # Create a database connection
        connection = self.db_connector.connect()

        # Execute a DELETE query to delete the medicine record
        query = "DELETE FROM medicines WHERE medicine_id = %s"
        values = (medicine_id,)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        print("Medicine deleted successfully.")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def register(self):
        # Implement admin registration logic

        # Prompt the user for input values

        # Validate input values

        # Create a database connection
        connection = self.db_connector.connect()

        # Execute an INSERT query to insert the admin record
        query = "INSERT INTO admins (name) VALUES (%s)"
        values = (name,)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        print("Admin registered successfully.")

    def login(self):
        # Implement admin login logic

        # Prompt the user for input values

        # Validate input values

        # Create a database connection
        connection = self.db_connector.connect()

        # Execute a SELECT query to check if the admin record exists
        query = "SELECT * FROM admins WHERE name = %s"
        values = (name,)
        cursor = connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            print("Admin login successful.")
        else:
            print("Invalid credentials.")

    def view_managers(self):
        # Implement logic to view all managers

        # Create a database connection
        connection = self.db_connector.connect()

        # Execute a SELECT query to retrieve manager records
        query = "SELECT * FROM managers"
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        # Display managers
        print("Managers:")
        for result in results:
            print(result)

    def view_all_medicines(self):
        # Implement logic to view all medicines

        # Create a database connection
        connection = self.db_connector.connect()

        # Execute a SELECT query to retrieve all medicine records
        query = "SELECT * FROM medicines"
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        # Display medicines
        print("All Medicines:")
        for result in results:
            print(result)
