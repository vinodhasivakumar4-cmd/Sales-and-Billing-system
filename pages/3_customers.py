import streamlit as st
from database import get_connection

st.set_page_config(
    page_title="Customers",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Customer Management")
st.write("Add and manage customer information.")

# Add Customer
st.subheader("➕ Add New Customer")

with st.form("customer_form"):

    name = st.text_input("Customer Name")

    col1, col2 = st.columns(2)

    with col1:
        phone = st.text_input("Phone Number")

    with col2:
        email = st.text_input("Email")

    submitted = st.form_submit_button("Add Customer")

    if submitted:

        if not name:
            st.error("Please enter customer name.")

        else:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO customers (name, phone, email)
                VALUES (?, ?, ?)
                """,
                (name, phone, email)
            )

            connection.commit()
            connection.close()

            st.success(f"{name} added successfully!")

            st.rerun()


# Display Customers
st.subheader("📋 Customer List")

connection = get_connection()

customers = connection.execute(
    """
    SELECT id, name, phone, email
    FROM customers
    ORDER BY id DESC
    """
).fetchall()

connection.close()


if customers:

    for customer in customers:

        customer_id, name, phone, email = customer

        col1, col2, col3, col4 = st.columns(
            [1, 3, 2, 3]
        )

        with col1:
            st.write(customer_id)

        with col2:
            st.write(name)

        with col3:
            st.write(phone)

        with col4:
            st.write(email)

else:

    st.info("No customers available. Add your first customer above.")