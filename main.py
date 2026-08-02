print("===== Stock Portfolio Tracker =====")
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 150
}
total = 0
while True:
    stock_name = input("\nEnter Stock Name (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))
        amount = stocks[stock_name] * quantity
        total = total + amount
        print("Price of", stock_name, "=", stocks[stock_name])
        print("Investment =", amount)
    else:
        print("Stock not available.")
print("\n--------------------------")
print("Total Investment =", total)
print("--------------------------")
file = open("portfolio.txt", "w")
file.write("Total Investment = " + str(total))
file.close()
print("Result saved in portfolio.txt")