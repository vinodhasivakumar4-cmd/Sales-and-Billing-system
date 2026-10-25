import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from analytics import (
    load_sales_data,
    sales_summary,
    product_analysis,
    customer_analysis,
    monthly_sales
)

st.set_page_config(
    page_title="Data Science Analytics",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Data Science Analytics")
st.write(
    "Analyze sales and billing data to discover useful business patterns."
)


# Load data
df = load_sales_data()


if df.empty:

    st.warning(
        "No sales data available. "
        "Generate at least one bill first."
    )

    st.stop()


# Summary
summary = sales_summary(df)

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Revenue",
        f"₹{summary['total_revenue']:,.2f}"
    )

with col2:
    st.metric(
        "Total Bills",
        summary["total_bills"]
    )

with col3:
    st.metric(
        "Quantity Sold",
        summary["total_quantity"]
    )

with col4:
    st.metric(
        "Average Bill",
        f"₹{summary['average_bill']:,.2f}"
    )


st.divider()


# Product analysis
st.subheader("📦 Product Analysis")

product_data = product_analysis(df)

st.dataframe(
    product_data,
    use_container_width=True
)


# Product revenue chart
fig1, ax1 = plt.subplots()

product_data["revenue"].plot(
    kind="bar",
    ax=ax1
)

ax1.set_title("Revenue by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Revenue")

plt.xticks(rotation=45)

st.pyplot(fig1)

plt.close(fig1)


# Customer analysis
st.subheader("👥 Customer Analysis")

customer_data = customer_analysis(df)

st.dataframe(
    customer_data,
    use_container_width=True
)


# Customer spending chart
fig2, ax2 = plt.subplots()

customer_data["total_spending"].plot(
    kind="bar",
    ax=ax2
)

ax2.set_title("Customer Spending")
ax2.set_xlabel("Customer")
ax2.set_ylabel("Amount Spent")

plt.xticks(rotation=45)

st.pyplot(fig2)

plt.close(fig2)


# Monthly analysis
st.subheader("📅 Monthly Sales Analysis")

monthly_data = monthly_sales(df)

st.dataframe(
    monthly_data,
    use_container_width=True
)


# Monthly revenue chart
if len(monthly_data) > 0:

    fig3, ax3 = plt.subplots()

    ax3.plot(
        monthly_data["month"],
        monthly_data["revenue"],
        marker="o"
    )

    ax3.set_title("Monthly Revenue Trend")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Revenue")

    plt.xticks(rotation=45)

    st.pyplot(fig3)

    plt.close(fig3)


# Raw dataset
st.subheader("📋 Sales Dataset")

st.dataframe(
    df,
    use_container_width=True
)


# Download
csv = df.to_csv(index=False)

st.download_button(
    "⬇️ Download Analytics Dataset",
    csv,
    "sales_analysis_dataset.csv",
    "text/csv"
)