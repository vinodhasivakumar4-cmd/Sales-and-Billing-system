import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales & Billing Dashboard")
st.write("Overview of your sales, products, customers, and revenue.")


# -------------------------
# Load database information
# -------------------------

connection = get_connection()

products_count = connection.execute(
    "SELECT COUNT(*) FROM products"
).fetchone()[0]

customers_count = connection.execute(
    "SELECT COUNT(*) FROM customers"
).fetchone()[0]

sales_count = connection.execute(
    "SELECT COUNT(*) FROM sales"
).fetchone()[0]

total_revenue = connection.execute(
    "SELECT COALESCE(SUM(final_amount), 0) FROM sales"
).fetchone()[0]

total_stock = connection.execute(
    "SELECT COALESCE(SUM(stock), 0) FROM products"
).fetchone()[0]

sales = pd.read_sql_query(
    """
    SELECT
        customer_name,
        final_amount,
        sale_date
    FROM sales
    ORDER BY sale_date
    """,
    connection
)

connection.close()


# -------------------------
# KPI Cards
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Products",
        products_count
    )

with col2:
    st.metric(
        "👥 Customers",
        customers_count
    )

with col3:
    st.metric(
        "🧾 Bills",
        sales_count
    )

with col4:
    st.metric(
        "💰 Revenue",
        f"₹{total_revenue:,.2f}"
    )


st.divider()


# -------------------------
# Inventory
# -------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📦 Inventory")

    st.metric(
        "Total Stock Available",
        total_stock
    )


with col2:

    st.subheader("💡 System Status")

    if products_count > 0 and customers_count > 0:
        st.success("System is ready for billing.")
    else:
        st.warning("Add products and customers to start billing.")


# -------------------------
# Revenue Chart
# -------------------------

if not sales.empty:

    st.divider()

    st.subheader("📈 Revenue Trend")

    sales["sale_date"] = pd.to_datetime(
        sales["sale_date"]
    )

    daily_sales = (
        sales
        .groupby(sales["sale_date"].dt.date)["final_amount"]
        .sum()
    )

    st.line_chart(daily_sales)


    # -------------------------
    # Customer Revenue
    # -------------------------

    st.subheader("👥 Customer Revenue")

    customer_revenue = (
        sales
        .groupby("customer_name")["final_amount"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(customer_revenue)

else:

    st.info(
        "No sales data available yet. "
        "Generate your first bill to see analytics."
    )