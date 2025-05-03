
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv('sales_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Add Day of Week and Month for time-based analysis
df['Day_of_Week'] = df['Date'].dt.day_name()
df['Month'] = df['Date'].dt.month_name()

# Display first few rows
print("First few rows:")
print(df.head())

# Total sales over time
plt.figure(figsize=(10,5))
sns.lineplot(x='Date', y='Total_Sales', data=df.groupby('Date').sum().reset_index())
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.savefig('total_sales_over_time.png')  # Saves the chart as an image
plt.show()

# Sales by category
plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Total_Sales', estimator=sum, ci=None, data=df)
plt.title('Total Sales by Category')
plt.ylabel('Total Sales')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top selling products
top_products = df.groupby('Product_Name')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\nTop Selling Products by Quantity Sold:")
print(top_products)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.index, y=top_products.values)
plt.title('Top Selling Products by Quantity Sold')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_selling_products.png')  # Save the chart as an image
plt.show()

# Sales by region
plt.figure(figsize=(8, 5))
sns.barplot(x='Region', y='Total_Sales', estimator=sum, ci=None, data=df)
plt.title('Total Sales by Region')
plt.ylabel('Total Sales')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_region.png')  # Save the chart as an image
plt.show()