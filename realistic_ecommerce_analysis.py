import pandas as pd 
import numpy as np 

np.random.seed(42)

num_orders= 1000

products = ["Laptop",
"Phone",
"Headphones",
"Sneakers",
"Backpack",
"Smartwatch"
]
categories = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Headphones": "Electronics",
    "Sneakers": "Fashion",
    "Backpack": "Fashion",
    "Smartwatch": "Electronics"
}

prices = {
    "Laptop": 850000,
    "Phone": 450000,
    "Headphones": 80000,
    "Sneakers": 65000,
    "Backpack": 35000,
    "Smartwatch": 120000
}

states = [
    "Lagos",
    "Abuja",
    "Rivers",
    "Anambra",
    "Oyo",
    "Enugu"
]

selected_products = np.random.choice(products, num_orders)

df = pd.DataFrame({
    "OrderID": range(1, num_orders + 1),
    "CustomerID": np.random.randint(1001,1301,num_orders),
    "Product": selected_products,
    "Quantity": np.random.randint(1, 6, num_orders),
    "State": np.random.choice(states, num_orders),
    "OrderDate": pd.date_range(
        start="2025-01-01",
        periods=num_orders,
        freq="D"
    )
})

df["Category"] = df["Product"].map(categories)
df["Price"] = df["Product"].map(prices)

df.to_csv("realistic_nigerian_ecommerce.csv", index=False)

print(df.head())
print("\nDataset Shape:", df.shape)

df = pd.read_csv("realistic_nigerian_ecommerce.csv")

df["Revenue"] = df["Price"] * df["Quantity"] 
total_revenue = df["Revenue"].sum()

total_orders = df["OrderID"].nunique()

total_products_sold = df["Quantity"].sum()

average_order_value = df["Revenue"].mean()

print("\n===== KPI REPORT =====")
print(f"Total Revenue: ₦{total_revenue:,.0f}")
print("Total Orders:", total_orders)
print("Products Sold:", total_products_sold)
print("Average Order Value:", average_order_value)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

df["Month"] = df["OrderDate"].dt.strftime("%b")

month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"
]

monthly_revenue = (
    df.groupby("Month")["Revenue"]
      .sum()
      .reindex(month_order)
)

print("\n===== MONTHLY REVENUE =====")
print(monthly_revenue)

top_customers = (
    df.groupby("CustomerID")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== TOP CUSTOMERS =====")
print(top_customers)


product_revenue = df.groupby("Product")["Revenue"].sum()
print(product_revenue.sort_values(ascending=False))

state_summary = (
    df.groupby("State")
      .agg({
          "Revenue":"sum",
          "Quantity":"sum",
          "OrderID":"count"
      })
      .sort_values("Revenue", ascending=False)
)

print("\n===== STATE SUMMARY =====")
print(state_summary)

state_revenue = df.groupby("State")["Revenue"].sum()

print(state_revenue.sort_values(ascending=False))

import matplotlib.pyplot as plt

product_revenue = (
    df.groupby("Product")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₦)")
plt.savefig("images/revenue_by_product.png")
plt.show()

state_revenue = (
    df.groupby("State")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

state_revenue.plot(kind="bar")

plt.title("Revenue by State")
plt.xlabel("State")
plt.ylabel("Revenue (₦)")
plt.savefig("revenue_by_state.png")
plt.show()

monthly_revenue.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₦)")
plt.savefig("images/monthly_revenue.png")
plt.show()

category_revenue = (
    df.groupby("Category")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(category_revenue)

category_revenue.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Revenue Distribution by Category")
plt.ylabel("")
plt.savefig("images/category_revenue.png")
plt.show()

print("\n===== BUSINESS INSIGHTS =====")

print(
    f"Highest revenue product: {product_revenue.idxmax()}"
)

print(
    f"Highest revenue state: {state_revenue.idxmax()}"
)

print(
    f"Top customer ID: {top_customers.index[0]}"
)