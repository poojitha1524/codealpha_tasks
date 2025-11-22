# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 140,
    "MSFT": 320,
    "GOOGL": 130
}

portfolio = {}

print("=== Simple Stock Portfolio Tracker ===")

# Input stocks from the user
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue

    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate investment
total_value = 0
print("\n--- Portfolio Summary ---")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print("\nTotal Portfolio Value: $", total_value)

# Optional: Save results to file
save = input("\nSave results to file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    with open(filename, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal Portfolio Value,{total_value}\n")

    print(f"✅ Results saved to {filename}")
