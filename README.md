# 🍔📦 OrderPlay — Food Delivery Data Engineering & Dashboard Project

OrderPlay is a data engineering and analytics project built using real-world food delivery data.
The project demonstrates the full workflow from raw CSV data to a PostgreSQL database and an interactive dashboard built with Streamlit.

---

## 🧠 Project Overview

This project focuses on understanding food delivery operations through data by:

- Cleaning and transforming raw delivery order data
- Designing a relational database schema
- Loading data into PostgreSQL
- Writing SQL queries for analysis
- Visualizing insights in an interactive dashboard

OrderPlay is designed as a **portfolio project for a Junior Data Engineer**, emphasizing clarity, structure, and real-world practices.

---

## 📊 Dataset Source

The dataset used in this project is publicly available on **Kaggle**:

- **Dataset Name:** Food Delivery Order History Data  
- **Author:** Sujal Suthar  
- **Platform:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data  

The dataset contains historical food delivery orders, including order details, restaurant information, delivery timing, pricing, and customer reviews.

> This dataset is used for educational and portfolio purposes only.

---

## 🏗️ Data Pipeline

```text
CSV Files
   ↓
Pandas (Data Cleaning & Transformation)
   ↓
PostgreSQL (Relational Database)
   ↓
SQL Analysis
   ↓
Streamlit Dashboard


## 🗃 Database Schema

The database is designed using a relational model with the following main tables:

restaurants

orders

order_items

order_finances

order_operations

order_reviews

The database schema is designed using a relational model and normalized up to Third Normal Form (3NF). The tables are implemented using SQL DDL with primary and foreign key constraints to ensure data integrity.

📈 Dashboard Features

The Streamlit dashboard provides the following insights:

📅 Orders per Day — daily order trends

📊 Order Status Distribution — delivered vs canceled orders

🍽 Best Seller Restaurants — restaurants with highest revenue

🕒 Recent Orders — latest order activities

⭐ Customer Reviews — sample real user reviews

The dashboard queries data directly from PostgreSQL using SQL.


▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/JirawitchJang/OrderPlay.git
cd OrderPlay

2️⃣ Create and activate virtual environment

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup PostgreSQL

Create a database named orderplay

5️⃣ Run the dashboard
streamlit run app/data_v.py

📝 Notes

condb.py centralizes database connection logic

SQL logic is separated from Python code for clarity

The project follows a clean separation between data, SQL, and application layers

📌 License

This project is created for educational and portfolio purposes.
All data credit belongs to the original dataset author.
# 🍔📦 OrderPlay — Food Delivery Data Engineering & Dashboard Project


