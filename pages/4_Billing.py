import streamlit as st
from database import get_connection

st.set_page_config(
    page_title="Billing",
    page_icon="🧾",
    layout="wide"
)

st.title("🧾 Create Bill")
st.write("Create a new customer bill and store the sale.")


# Get customers
connection = get_connection()

customers = connection.execute(
    "SELECT id, name FROM customers ORDER BY name"
).fetchall()

# Get products
products = connection.execute(
    "SELECT id, name, price, stock FROM products WHERE stock > 0 ORDER BY name"
).fetchall()

connection.close()


# Check required data
if not customers:
    st.warning("Please add at least one customer before creating a bill.")
    st.stop()

if not products:
    st.warning("Please add at least one product with available stock.")
    st.stop()


# Customer selection
st.subheader("👤 Customer")

customer_names = [customer[1] for customer in customers]

selected_customer = st.selectbox(
    "Select Customer",
    customer_names
)


# Product selection
st.subheader("📦 Product")

product_names = [product[1] for product in products]

selected_product = st.selectbox(
    "Select Product",
    product_names
)


# Find selected product
selected_product_data = next(
    product for product in products
    if product[1] == selected_product
)

product_id = selected_product_data[0]
product_price = selected_product_data[2]
available_stock = selected_product_data[3]


st.write(f"**Price:** ₹{product_price:,.2f}")
st.write(f"**Available Stock:** {available_stock}")


quantity = st.number_input(
    "Quantity",
    min_value=1,
    max_value=available_stock,
    value=1,
    step=1
)


# Discount
discount_percent = st.number_input(
    "Discount (%)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0
)


# Tax
tax_percent = st.number_input(
    "Tax (%)",
    min_value=0.0,
    max_value=100.0,
    value=18.0,
    step=1.0
)


# Calculate bill
subtotal = product_price * quantity

discount_amount = subtotal * discount_percent / 100

amount_after_discount = subtotal - discount_amount

tax_amount = amount_after_discount * tax_percent / 100

final_amount = amount_after_discount + tax_amount


st.subheader("💰 Bill Summary")

col1, col2 = st.columns(2)

with col1:
    st.write(f"Subtotal: ₹{subtotal:,.2f}")
    st.write(f"Discount: ₹{discount_amount:,.2f}")
    st.write(f"Tax: ₹{tax_amount:,.2f}")

with col2:
    st.metric(
        "Final Amount",
        f"₹{final_amount:,.2f}"
    )


# Create bill
if st.button("🧾 Generate Bill", type="primary"):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Insert sale
        cursor.execute(
            """
            INSERT INTO sales
            (
                customer_name,
                total_amount,
                discount,
                tax,
                final_amount
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                selected_customer,
                subtotal,
                discount_amount,
                tax_amount,
                final_amount
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
                selected_product,
                quantity,
                product_price,
                subtotal
            )
        )

        # Update product stock
        cursor.execute(
            """
            UPDATE products
            SET stock = stock - ?
            WHERE id = ?
            """,
            (
                quantity,
                product_id
            )
        )

        connection.commit()

        st.success(f"Bill #{sale_id} generated successfully!")

        st.divider()

        st.subheader("🧾 Invoice")

        st.write(f"**Bill Number:** {sale_id}")
        st.write(f"**Customer:** {selected_customer}")
        st.write(f"**Product:** {selected_product}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Price:** ₹{product_price:,.2f}")
        st.write(f"**Subtotal:** ₹{subtotal:,.2f}")
        st.write(f"**Discount:** ₹{discount_amount:,.2f}")
        st.write(f"**Tax:** ₹{tax_amount:,.2f}")

        st.markdown(
            f"### Total Amount: ₹{final_amount:,.2f}"
        )

    except Exception as error:

        connection.rollback()

        st.error(
            f"Unable to generate bill: {error}"
        )

    finally:

        connection.close()