import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("superstore.csv", encoding='latin1')

print("Dataset Preview:")
print(df.head())

category_sales = df.groupby('Category')['Sales'].sum().reset_index()
sns.barplot(data=category_sales, x='Category', y='Sales')
plt.title("Total Sales by Category")
plt.tight_layout()
plt.show()

region_profit = df.groupby('Region')['Profit'].sum().reset_index()
sns.barplot(data=region_profit, x='Region', y='Profit')
plt.title("Profit by Region")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x='Sales', y='Profit', hue='Category')
plt.title("Sales vs Profit by Category")
plt.tight_layout()
plt.show()

sns.histplot(data=df, x='Discount', bins=10, kde=True)
plt.title("Discount Distribution")
plt.tight_layout()
plt.show()
