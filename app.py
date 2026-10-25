import streamlit as st

st.set_page_config(
    page_title="Sales & Billing Management System",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* =========================
   MAIN APP
========================= */

.stApp {
    background-color: #000000;
    color: #ffffff;
}

/* Main content */
.main-title {
    color: #ffffff;
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    color: #d1d5db;
    font-size: 18px;
    margin-bottom: 25px;
}


/* =========================
   HERO
========================= */

.hero {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 40px;
    border-radius: 20px;
    border: 1px solid #374151;
    margin-bottom: 30px;
}

.hero-title {
    color: #ffffff;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero-text {
    color: #d1d5db;
    font-size: 17px;
    line-height: 1.7;
}


/* =========================
   SECTION TITLE
========================= */

.section-title {
    color: #ffffff;
    font-size: 28px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 18px;
}


/* =========================
   CARDS
========================= */

.card {
    background-color: #111111;
    padding: 25px;
    border-radius: 16px;
    min-height: 175px;
    border: 1px solid #333333;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}

.card-icon {
    font-size: 34px;
    margin-bottom: 12px;
}

.card-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
}

.card-text {
    color: #d1d5db;
    font-size: 15px;
    line-height: 1.6;
}


/* =========================
   STATUS
========================= */

.status {
    background-color: #111111;
    padding: 20px 25px;
    border-radius: 15px;
    border-left: 5px solid #22c55e;
    border-top: 1px solid #333333;
    border-right: 1px solid #333333;
    border-bottom: 1px solid #333333;
    margin-top: 30px;
}

.status-title {
    color: #ffffff;
    font-size: 18px;
    font-weight: 700;
}

.status-text {
    color: #d1d5db;
    margin-top: 8px;
}


/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"] {
    background-color: #0a0a0a;
    border-right: 1px solid #333333;
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}


/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;
    color: #9ca3af;
    margin-top: 35px;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">Sales & Billing Management System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A smart platform to manage products, customers, billing and sales analytics.'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# HERO
# =========================

st.markdown(
    '<div class="hero">'
    '<div class="hero-title">Welcome to  Sales Dashboard </div>'
    '<div class="hero-text">'
    'Manage your business operations from one place.<br>'
    'Track products, create bills, manage customers and understand your sales performance.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# FEATURES
# =========================

st.markdown(
    '<div class="section-title"> System Features</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="card">'
        '<div class="card-icon">📦</div>'
        '<div class="card-title">Product Management</div>'
        '<div class="card-text">'
        'Add products, manage prices, categories and monitor available stock.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="card">'
        '<div class="card-icon">👥</div>'
        '<div class="card-title">Customer Management</div>'
        '<div class="card-text">'
        'Maintain customer information including names, phone numbers and email addresses.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="card">'
        '<div class="card-icon">🧾</div>'
        '<div class="card-title">Billing System</div>'
        '<div class="card-text">'
        'Generate bills with discounts, taxes and automatic payment calculations.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


st.write("")


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="card">'
        '<div class="card-icon">📊</div>'
        '<div class="card-title">Sales Dashboard</div>'
        '<div class="card-text">'
        'Get an overview of revenue, customers, products and transactions.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="card">'
        '<div class="card-icon">📈</div>'
        '<div class="card-title">Sales Analysis</div>'
        '<div class="card-text">'
        'Analyze sales trends, customer revenue and transaction history.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="card">'
        '<div class="card-icon">💡</div>'
        '<div class="card-title">Business Insights</div>'
        '<div class="card-text">'
        'Understand business performance using data-driven sales information.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================
# SYSTEM STATUS
# =========================

st.markdown(
    '<div class="status">'
    '<div class="status-title">🟢 System Status</div>'
    '<div class="status-text">'
    'Application is running successfully. Use the sidebar to navigate through the system.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# FOOTER
# =========================

st.markdown(
    '<div class="footer">'
    'Sales & Billing Management System • Data Science Project'
    '</div>',
    unsafe_allow_html=True
)