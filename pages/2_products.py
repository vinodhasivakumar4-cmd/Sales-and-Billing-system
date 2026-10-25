import streamlit as st
from database import get_connection

st.set_page_config(
    page_title="Products",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Product Management")
st.write("Add and manage products in your inventory.")

# Add Product
st.subheader("➕ Add New Product")

with st.form("product_form"):
    name = st.text_input("Product Name")
    category = st.text_input("Category")
    
    col1, col2 = st.columns(2)

    with col1:
        price = st.number_input(
            "Price",
            min_value=0.0,
            step=0.01
        )

    with col2:
        stock = st.number_input(
            "Stock Quantity",
            min_value=0,
            step=1
        )

    submitted = st.form_submit_button("Add Product")

    if submitted:
        if not name or not category:
            st.error("Please enter product name and category.")
        else:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO products (name, category, price, stock)
                VALUES (?, ?, ?, ?)
                """,
                (name, category, price, stock)
            )

            connection.commit()
            connection.close()

            st.success(f"{name} added successfully!")
            st.rerun()


# Display Products
st.subheader("📋 Product Inventory")

connection = get_connection()

products = connection.execute(
    """
    SELECT id, name, category, price, stock
    FROM products
    ORDER BY id DESC
    """
).fetchall()

connection.close()

if products:
    for product in products:
        product_id, name, category, price, stock = product

        col1, col2, col3, col4, col5 = st.columns(
            [1, 3, 2, 2, 2]
        )

        with col1:
            st.write(product_id)

        with col2:
            st.write(name)

        with col3:
            st.write(category)

        with col4:
            st.write(f"₹{price:,.2f}")

        with col5:
            st.write(stock)

else:
    st.info("No products available. Add your first product above.")