import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(__file__), "../year_sales.csv")

data = pd.read_csv(path)

sorted_data = data.sort_values("NA_Sales", ascending=True)

x = sorted_data["Year"][:7]
y = sorted_data["NA_Sales"][:7]

plt.bar(x, y)
plt.show()