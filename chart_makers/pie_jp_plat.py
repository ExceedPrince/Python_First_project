import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(__file__), "../platform_sales.csv")

data = pd.read_csv(path)

sorted_data = data.sort_values("JP_Sales", ascending=False)

platforms = sorted_data["Platform"][:5]
sales = sorted_data["JP_Sales"][:5]

plt.pie(sales, labels=platforms, autopct='%.1f%%')
plt.show()

