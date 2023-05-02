import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(__file__), "../genre_sales.csv")

data = pd.read_csv(path)

sorted_data = data.sort_values("EU_Sales", ascending=False)

genres = sorted_data["Genre"][:3]
sales = sorted_data["EU_Sales"][:3]

plt.pie(sales, labels=genres, autopct='%.1f%%')
plt.show()