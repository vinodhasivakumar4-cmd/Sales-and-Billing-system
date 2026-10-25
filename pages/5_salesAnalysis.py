import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(
    page_title="Sales Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analysis")
st.write("Analyze sales and billing transactions.")


# Load sales data
connection = get_connection()

sales = pd.read_sql_query(
    """
    SELECT
        id AS Bill_ID,
        customer_name AS Customer,
        total_amount AS Subtotal,
        discount AS Discount,
        tax AS Tax,
        final_amount AS Final_Amount,
        sale_date AS Sale_Date
    FROM sales
    ORDER BY id DESC
    """,
    connection
)

connection.close()


# No sales
if sales.empty:
    st.info("No sales available yet. Generate a bill first.")
    st.stop()


# Convert date
sales["Sale_Date"] = pd.to_datetime(sales["Sale_Date"])


# -------------------------
# KPI section
# -------------------------

total_revenue = sales["Final_Amount"].sum()

total_bills = len(sales)

average_bill = sales["Final_Amount"].mean()

total_discount = sales["Discount"].sum()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Revenue",
        f"₹{total_revenue:,.2f}"
    )

with col2:
    st.metric(
        "🧾 Total Bills",
        total_bills
    )

with col3:
    st.metric(
        "📈 Average Bill",
        f"₹{average_bill:,.2f}"
    )

with col4:
    st.metric(
        "🏷️ Total Discount",
        f"₹{total_discount:,.2f}"
    )


st.divider()


# -------------------------
# Sales table
# -------------------------

st.subheader("📋 Sales History")

st.dataframe(
    sales,
    use_container_width=True
)


# -------------------------
# Revenue chart
# -------------------------

st.subheader("📈 Revenue by Bill")

chart_data = sales[
    ["Bill_ID", "Final_Amount"]
].set_index("Bill_ID")

st.line_chart(chart_data)


# -------------------------
# Customer analysis
# -------------------------

st.subheader("👥 Customer-wise Revenue")

customer_sales = (
    sales.groupby("Customer")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(customer_sales)


# -------------------------
# Download dataset
# -------------------------

st.subheader("⬇️ Download Sales Dataset")

csv_data = sales.to_csv(index=False)

st.download_button(
    label="Download Sales CSV",
    data=csv_data,
    file_name="sales_data.csv",
    mime="text/csv"
)