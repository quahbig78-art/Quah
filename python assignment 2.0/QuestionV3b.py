import pandas as pd
import matplotlib.pyplot as plt

portfolio_df = pd.read_csv(
    "portfolio_analysis.csv"
)

plt.figure(figsize=(8,5))

plt.bar(
    portfolio_df["Ticker"],
    portfolio_df["Return Percentage"]
)

plt.title("Return Percentage Comparison")
plt.xlabel("Stock")
plt.ylabel("Return Percentage (%)")

plt.grid(True)

plt.show()