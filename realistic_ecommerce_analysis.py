import pandas as pd 
import numpy as np 

np.random.seed(42)

num_orders= 1000

products = ["Laptop",
"Phone",
"Headphones",
"sneakers",
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
print("Total Revenue:")
print(df["Revenue"].sum())
product_revenue = df.groupby("Product")["Revenue"].sum()
print(product_revenue.sort_values(ascending=False))

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
plt.show()

category_revenue = (
    df.groupby("Category")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(category_revenue)