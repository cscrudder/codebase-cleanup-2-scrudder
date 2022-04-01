from app.alphavantage_service import fetch_crypto_data

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"

print("CRYPTO REPORT...")

tsd = fetch_crypto_data(symbol)

from app.utils import to_usd

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
#print(latest)
# not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
