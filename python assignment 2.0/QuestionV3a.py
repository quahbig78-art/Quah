import yfinance as yf
import matplotlib.pyplot as plt

tickers = {
    "Maybank": "1155.KL",
    "CIMB": "1023.KL",
    "Public Bank": "1295.KL",
    "Tenaga": "5347.KL",
    "Petronas Chemicals": "5183.KL"
}

plt.figure(figsize=(12,6))

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