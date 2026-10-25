import sqlite3
import random
from datetime import datetime, timedelta

DATABASE_NAME = "sales_billing.db"

products = [
    ("Laptop", "Electronics", 50000, 50),
    ("Mouse", "Electronics", 800, 100),
    ("Keyboard", "Electronics", 1500, 80),
    ("Headphones", "Electronics", 2500, 70),
    ("Monitor", "Electronics", 12000, 40),
    ("USB Cable", "Accessories", 400, 120),
    ("Power Bank", "Accessories", 1800, 60),
    ("Notebook", "Stationery", 100, 200),
    ("Pen", "Stationery", 30, 300),
    ("Backpack", "Bags", 1800, 75),
]

customers = [
    ("Arun", "9876543210", "arun@gmail.com"),
    ("Priya", "9876543211", "priya@gmail.com"),
    ("Rahul", "9876543212", "rahul@gmail.com"),
    ("Divya", "9876543213", "divya@gmail.com"),
    ("Karthik", "9876543214", "karthik@gmail.com"),
    ("Anitha", "9876543215", "anitha@gmail.com"),
    ("Sanjay", "9876543216", "sanjay@gmail.com"),
    ("Meena", "9876543217", "meena@gmail.com"),
    ("Vijay", "9876543218", "vijay@gmail.com"),
    ("Keerthi", "9876543219", "keerthi@gmail.com"),
]


def generate_data():

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Clear old sample data
    cursor.execute("DELETE FROM sale_items")
    cursor.execute("DELETE FROM sales")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM customers")

    # Reset IDs
    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='products'"
    )

    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='customers'"
    )

    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='sales'"
    )

    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='sale_items'"
    )

    # Insert products
    for product in products:

        cursor.execute(
            """
            INSERT INTO products
            (name, category, price, stock)
            VALUES (?, ?, ?, ?)
            """,
            product
        )

    # Insert customers
    for customer in customers:

        cursor.execute(
            """
            INSERT INTO customers
            (name, phone, email)
            VALUES (?, ?, ?)
            """,
            customer
        )

    connection.commit()

    # Generate 100 sales
    for i in range(100):

        customer = random.choice(customers)[0]

        product = random.choice(products)

        product_name = product[0]
        price = product[2]

        quantity = random.randint(1, 5)

        subtotal = price * quantity

        discount_percent = random.choice(
            [0, 0, 0, 5, 10, 15]
        )

        discount = subtotal * discount_percent / 100

        amount_after_discount = subtotal - discount

        tax = amount_after_discount * 0.18

        final_amount = amount_after_discount + tax

        # Generate dates across previous 6 months
        days_ago = random.randint(0, 180)

        sale_date = (
            datetime.now() - timedelta(days=days_ago)
        ).strftime("%Y-%m-%d %H:%M:%S")

        # Insert sale
        cursor.execute(
            """
            INSERT INTO sales
            (
                customer_name,
                total_amount,
                discount,
                tax,
                final_amount,
                sale_date
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                customer,
                subtotal,
                discount,
                tax,
                final_amount,
                sale_date
            )
        )

        sale_id = cursor.lastrowid

        # Insert sale item
        cursor.execute(
            """
            INSERT INTO sale_items
            (
                sale_id,
                product_name,
                quantity,
                price,
                subtotal
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                sale_id,
                product_name,
                quantity,
                price,
                subtotal
            )
        )

    connection.commit()
    connection.close()

    print("Sample data generated successfully!")
    print("10 products added.")
    print("10 customers added.")
    print("100 sales transactions added.")


if __name__ == "__main__":
    generate_data()