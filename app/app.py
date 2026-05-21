import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("Sales Dashboard")

# Load Dataset
df = pd.read_csv('../dataset/train.csv')

# Clean Data
df = df.dropna()

# Convert Date
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# KPI Metrics
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()

# Display KPIs
st.subheader("Key Business Metrics")

st.write(f"Total Sales: {total_sales:,.2f}")
st.write(f"Average Sales: {average_sales:,.2f}")
st.write(f"Highest Sale: {max_sales:,.2f}")

# Sales by Category
st.subheader("Sales by Category")

category_sales = df.groupby('Category')['Sales'].sum()

fig1, ax1 = plt.subplots(figsize=(8,5))
ax1.bar(category_sales.index, category_sales.values)

ax1.set_title("Sales by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Sales")

st.pyplot(fig1)

# Top 10 States
st.subheader("Top 10 States by Sales")

state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(12,6))
ax2.bar(state_sales.index, state_sales.values)

ax2.set_title("Top 10 States by Sales")
ax2.set_xlabel("States")
ax2.set_ylabel("Sales")

plt.xticks(rotation=45)

st.pyplot(fig2)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.plot(monthly_sales.index, monthly_sales.values)

ax3.set_title("Monthly Sales Trend")
ax3.set_xlabel("Month")
ax3.set_ylabel("Sales")

st.pyplot(fig3)