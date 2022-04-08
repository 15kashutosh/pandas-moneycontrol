import json

data = json.load(open("D:\PycharmProjects\AdvancePythonPractice\pandas-moneycontrol\data\stock_prices.json"))
print(data)

#user input for checking stock price:
def stock_input():
    stock_name = input("Enter the Company's name: ")
    while stock_name.isalnum() ==False and ' ' not in stock_name:
        stock_name = input("Enter the Company's name: ")

    stock_price = input("Enter the Company's price: ")
    while stock_price.isdigit() == False:
        stock_price = input("Enter the Company's price: ")
    return stock_name,int(stock_price)

#stock_input comparison with the current market details:
def stock_comparision(stock_name,stock_price):
    print(stock_name,stock_price)
    # result = data.get(stock_name)
    #print(result)
    if stock_name in data.keys():
        if ',' in data[stock_name]:
            market_price = float(data[stock_name].replace(',',''))
        else:
            market_price = float(data[stock_name])
        if stock_price>market_price:
            print(f"Time to buy {stock_name}")
            print(f"{stock_name}'s  Last Traded Price : {data[stock_name]}")
        else:
            print("Price criteria not satisfied")
    else:
        print("Stock is not part of NSE 500 companies")

#Function call for stock comparision and dispalying results:
stock_name,stock_price = stock_input()
stock_comparision(stock_name,stock_price)