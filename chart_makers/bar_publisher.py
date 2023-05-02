import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.join(os.path.dirname(__file__), "../publisher_sales.csv")

data = pd.read_csv(path)

sorted_data = data.sort_values("Global_Sales", ascending=False)

x = sorted_data["Publisher"][:5]
y = sorted_data["Global_Sales"][:5]

plt.bar(x, y)
plt.show()