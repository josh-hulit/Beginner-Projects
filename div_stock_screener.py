
stock_name = input("Stock Ticker: ")
pe_ratio = float(input("PE Ratio: "))
div_yield = float(input("Div Yield: "))
mkt_price = float(input("Current Price: "))
cost_basis = float(input("Cost per Share: "))


print(stock_name)

gain = (int(mkt_price - cost_basis)/mkt_price)
percent_gain = gain * 100
print(f"Percent Gain {int(percent_gain)}%")

if cost_basis > mkt_price and pe_ratio < 10 and div_yield > 1:
    print("Buy")

else:
    print("Hold")
