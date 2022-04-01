from app.utils import to_usd
from app.alphavantage_service import fetch_stock_data

symbol = input("Please input a stock symbol (default: 'NFLX'): ") or "NFLX"

df = fetch_stock_data(symbol)

print("STOCKS REPORT...")

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
