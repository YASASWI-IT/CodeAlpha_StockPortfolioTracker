# Stock Portfolio Tracker - CodeAlpha Task 2

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 170
}

print("📊 Welcome to Stock Portfolio Tracker")

total_investment = 0
portfolio = []

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        try:
            quantity = int(input("Enter quantity: "))
            cost = stock_prices[stock] * quantity

            total_investment += cost

            portfolio.append(
                f"{stock} | Quantity: {quantity} | Value: ₹{cost}"
            )

            print(f"Added: {stock} x {quantity} = ₹{cost}")

        except ValueError:
            print("⚠️ Please enter a valid number for quantity.")
    else:
        print("❌ Stock not found in database.")

print("\n============================")
print(f"💰 Total Investment Value: ₹{total_investment}")
print("============================")

# Save report to file
with open("portfolio_report.txt", "w", encoding="utf-8") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=========================\n")

    for item in portfolio:
        file.write(item + "\n")

    file.write("=========================\n")
    file.write(f"Total Investment Value: ₹{total_investment}")
    
print("📄 Report saved as portfolio_report.txt")
print("Thank you for using Stock Tracker 🚀")