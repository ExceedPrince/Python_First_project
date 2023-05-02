import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(__file__), "../year_sales.csv")

data = pd.read_csv(path)

sorted_data = data.sort_values("Global_Sales", ascending=False)

years = sorted_data["Year"][:6]
sales = sorted_data["Global_Sales"][:6]

fig, ax = plt.subplots()
ax.plot(years, sales, 'o', markersize=15)
ax.set(xlabel='Year', ylabel='Global Sales', title='The 6 Biggest Global Sales')
plt.show()