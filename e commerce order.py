import pandas as pd
import matplotlib.pyplot as plt

# Sample dummy e-commerce order data


data = pd.read_csv(r"C:\Users\lenovo\Desktop\order details.csv", encoding="ISO-8859-1")

print(data.head())  # Display first few rows




# Convert data to DataFrame
df = pd.DataFrame(data)


# Basic Data Insights
print("Total Orders:", df['Order ID'].nunique())  # Count unique orders
print("Total Revenue:", df['Amount'].sum())  
print("Average Order Value (AOV):", df['Amount'].mean())  

# Sales by Category
category_counts = df["Category"].value_counts()
print("Top Product Categories:\n", category_counts)

category_counts.plot(kind="pie", title="Sales by Category",autopct="%1.1f%%", color="red")
plt.xlabel("Category")
plt.show()



#Top selling product
Top_product=df.groupby('Product Name')['Amount'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,4))
Top_product.plot(kind='bar',color='blue',title= "Top selling products")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

#monthly sales trend

df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y", errors="coerce")
# Convert Date column to datetime
df["Month"] = df["Order Date"].dt.to_period("M")  # Extract Month
monthly_sales = df.groupby("Month")["Total Sales"].sum()
print("Monthly Sales Trend:\n", monthly_sales)


monthly_sales.plot(kind="bar", title="Monthly Sales Trend", color="green")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


#daily sales trend
df["Hour"] =df["Order Date"].dt.hour
df["Day"] =df["Order Date"].dt.day_name()

daily_sales =df.groupby(df['Order Date'].dt.date)['Total Sales'].sum()
print("daily Sales Trend:\n", daily_sales)
daily_sales.plot(kind="line", title="daily Sales Trend", marker="o" ,color="orange")
plt.xlabel("daily")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# Sales Distribution by Payment Method
payment_sales = df.groupby('payment_type')['Amount'].sum()
payment_sales.plot(kind='pie', title='Sales Distribution by Payment Method', autopct='%1.1f%%')
plt.show()


# Geographic Sales Distribution 

State_sales = df.groupby('State')['Amount'].sum()

State_sales.plot(kind='bar', title='Geographic Sales Distribution', color='brown')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()








