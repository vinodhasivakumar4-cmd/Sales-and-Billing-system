import pandas as pd
from database import get_connection


def load_sales_data():
    connection = get_connection()

    query = """
        SELECT
            s.id AS bill_id,
            s.customer_name,
            si.product_name,
            si.quantity,
            si.price,
            si.subtotal,
            s.discount,
            s.tax,
            s.final_amount,
            s.sale_date
        FROM sales s
        JOIN sale_items si
        ON s.id = si.sale_id
        ORDER BY s.sale_date
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    if not df.empty:
        df["sale_date"] = pd.to_datetime(df["sale_date"])

    return df


def sales_summary(df):

    if df.empty:
        return {}

    return {
        "total_revenue": df["final_amount"].sum(),
        "total_bills": df["bill_id"].nunique(),
        "total_quantity": df["quantity"].sum(),
        "average_bill": df.groupby("bill_id")["final_amount"]
        .first()
        .mean(),
        "total_discount": df["discount"].sum()
    }


def product_analysis(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("product_name")
        .agg(
            quantity_sold=("quantity", "sum"),
            revenue=("subtotal", "sum")
        )
        .sort_values(
            "revenue",
            ascending=False
        )
    )

    return result


def customer_analysis(df):

    if df.empty:
        return pd.DataFrame()

    result = (
        df.groupby("customer_name")
        .agg(
            total_quantity=("quantity", "sum"),
            total_spending=("final_amount", "sum")
        )
        .sort_values(
            "total_spending",
            ascending=False
        )
    )

    return result


def monthly_sales(df):

    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    df["month"] = df["sale_date"].dt.to_period("M").astype(str)

    result = (
        df.groupby("month")
        .agg(
            revenue=("final_amount", "sum"),
            quantity=("quantity", "sum")
        )
        .reset_index()
    )

    return result