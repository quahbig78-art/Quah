import yfinance as yf
import pandas as pd

# Bursa Malaysia stocks
tickers = {
    "Maybank": "1155.KL",
    "CIMB": "1023.KL",
    "Public Bank": "1295.KL",
    "Tenaga Nasional": "5347.KL",
    "Petronas Chemicals": "5183.KL"
}

investment = 1000

results = []

for company, ticker in tickers.items():

    try:
        print(f"Processing {ticker}...")

        df = yf.download(
            ticker,
            period="1mo",
            progress=False,
            auto_adjust=True
        )

        # Remove missing values
        df = df.dropna()

        # Check if enough data exists
        if len(df) < 2:
            print(f"{ticker}: Not enough data available")
            continue

        # Get Close prices
        close_prices = df["Close"].squeeze()

        previous_close = close_prices.iloc[-2]
        latest_close = close_prices.iloc[-1]

        daily_return = latest_close - previous_close

        shares_purchasable = investment / previous_close

        estimated_total_return = (
            shares_purchasable * daily_return
        )

        return_percentage = (
            estimated_total_return / investment
        ) * 100

        results.append([
            company,
            ticker,
            round(previous_close, 2),
            round(latest_close, 2),
            round(daily_return, 2),
            round(shares_purchasable, 2),
            round(estimated_total_return, 2),
            round(return_percentage, 2)
        ])

    except Exception as e:
        print(f"Error processing {ticker}: {e}")

# Create DataFrame
portfolio_df = pd.DataFrame(
    results,
    columns=[
        "Company",
        "Ticker",
        "Previous Closing Price",
        "Latest Closing Price",
        "Daily Return",
        "Shares Purchasable",
        "Estimated Total Return",
        "Return Percentage"
    ]
)

print("\n===== Portfolio Analysis =====")
print(portfolio_df)

# Save to CSV
portfolio_df.to_csv(
    "portfolio_analysis.csv",
    index=False
)

print("\nData saved to portfolio_analysis.csv")

import yfinance as yf
import matplotlib.pyplot as plt

tickers = {
    "Maybank": "1155.KL",
    "CIMB": "1023.KL",
    "Public Bank": "1295.KL",
    "Tenaga Nasional": "5347.KL",
    "Petronas Chemicals": "5183.KL"
}

plt.figure(figsize=(12, 6))

for company, ticker in tickers.items():

    df = yf.download(
        ticker,
        period="1mo",
        progress=False,
        auto_adjust=True
    )

    plt.plot(
        df.index,
        df["Close"],
        label=company
    )

plt.title("Closing Price Trend of Bursa Malaysia Stocks (1 Month)")
plt.xlabel("Date")
plt.ylabel("Closing Price (RM)")
plt.legend()
plt.grid(True)

plt.show()