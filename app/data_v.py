import pandas as pd
import streamlit as st
from app.condb import get_engine

engine = get_engine()

def order_per_day(engine):
    return  pd.read_sql("""
    SELECT 
        DATE(order_placed_at) AS order_date,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY order_date
    ORDER BY order_date;
""",con = engine)

def order_status(engine):
    return pd.read_sql("""
    SELECT
        order_status,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY order_status;
""",con = engine)



def recent_orders(engine):
    return pd.read_sql("""
    SELECT 
        order_id,
        order_placed_at,
        order_status
    FROM orders
    ORDER BY order_placed_at DESC
    LIMIT 10;
""",con = engine)

def all_restaurant(engine):
    return pd.read_sql("""
    SELECT
        restaurant_id,
        restaurant_name,
        subzone,
        city
    FROM restaurants
""",con = engine)

def res_best_sell(engine):
    return pd.read_sql("""
    SELECT
        r.restaurant_id,
        r.restaurant_name,
        r.subzone,
        r.city,
        SUM(ofi.bill_subtotal + ofi.packaging_charges) AS total_revenue
    FROM orders o
    JOIN restaurants r
        ON o.restaurant_id = r.restaurant_id
    JOIN order_finances ofi
        ON o.order_id = ofi.order_id
    GROUP BY
        r.restaurant_id,
        r.restaurant_name
    ORDER BY total_revenue DESC;
""",con = engine)

def review(engine):
    return pd.read_sql("""
        SELECT
            order_id,
            rating,
            review
        FROM order_reviews
        WHERE review <> 'No Review'
        ORDER BY rating DESC ;         
""",con = engine)


st.title("OrderPlay Dashboard")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Recent Orders")
    df_recent = recent_orders(engine)
    st.dataframe(df_recent)

with col2:
    st.subheader("Order Status")
    df_status = order_status(engine)
    st.bar_chart(df_status.set_index("order_status"))


st.subheader("Orders per Day")
df_day = order_per_day(engine)
st.line_chart(df_day.set_index("order_date"))

st.subheader("All Restaurant Partners")
df_res = all_restaurant(engine)
st.dataframe(df_res.set_index("restaurant_id"))

st.subheader("Restaurant Best Seller")
df_bs = res_best_sell(engine)
st.dataframe(df_bs.set_index("restaurant_id"))

st.subheader("Review From Customer")
df_rw = review(engine)
st.dataframe(df_rw.set_index("order_id"))