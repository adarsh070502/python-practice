import os
from dotenv import load_dotenv
import psycopg2


class DatabaseManagement:

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Loading the values
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")

        # Connect to database
        self.conn, self.cursor = self.create_cursor()

    def create_cursor(self):

        # Connecting
        try:
            conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            print("Database connection successful!")

            # Create a cursor object
            cursor = conn.cursor()

            return conn, cursor

        except Exception as e:
            raise Exception(e)

    def create_table(self):
        try:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS products (
                    product_id SERIAL PRIMARY KEY,
                    product_name VARCHAR(100) NOT NULL,
                    quantity INT NOT NULL,
                    mrp NUMERIC(10, 2) NOT NULL,
                    tax NUMERIC(5, 2) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            self.cursor.execute(create_table_query)
            print("Table created successfully!")
        except Exception as e:
            raise Exception(e)

    def insert_data(self, data):
        # SQL query for inserting data
        insert_query = """
               INSERT INTO products (product_name, quantity, mrp, tax)
               VALUES (%s, %s, %s, %s);
               """

        # Insert multiple rows
        self.cursor.executemany(insert_query, data)
        self.conn.commit()  # Commit the transaction
        print(f"{self.cursor.rowcount} rows inserted successfully!")

    def fetch_product_by_id(self, product_id):
        # SQL query to fetch the row
        select_query = """
                SELECT * FROM products WHERE product_id = %s;
                """
        self.cursor.execute(select_query, (product_id,))

        # Fetch the result
        row = self.cursor.fetchone()
        return row


if __name__ == "__main__":
    db = DatabaseManagement()
    # sample_data = [
    #     ["Laptop", 10, 59999.99, 18.00],
    #     ["Mouse", 50, 499.99, 5.00],
    #     ["Keyboard", 30, 999.99, 12.00],
    #     ["Monitor", 15, 15999.99, 18.00],
    #     ["Printer", 5, 7999.99, 18.00],
    #     ["Desk", 20, 9999.99, 28.00],
    #     ["Chair", 40, 4999.99, 28.00],
    #     ["Router", 25, 1999.99, 5.00],
    #     ["Headphones", 35, 2999.99, 12.00],
    #     ["Webcam", 12, 2499.99, 18.00]
    # ]
    # db.create_table()
    # db.insert_data(sample_data)
    db.fetch_product_by_id(15)