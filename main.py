import requests
import bs4
import json

data = requests.get('https://www.moneycontrol.com/markets/indian-indices/top-nse-500-companies-list/7?classic=true')
# print(data.text)

soup = bs4.BeautifulSoup(data.text, 'lxml')
#print(soup)
#print(soup.select('.barLink')[0])
Company = []
for i in range(len(soup.select('.barLink'))):
    Company.append(soup.select('.barLink')[i].text)

LTP = []
for i in soup.select('td')[3::5]:
    if i.text != '':
        LTP.append(i.text)
company_prices = {}
for i in range(len(Company)):
    company_prices[Company[i]] = LTP[i]

json_obj = json.dumps(company_prices)
with open("D:\PycharmProjects\AdvancePythonPractice\pandas-moneycontrol\data\stock_prices.json", "w") as file:
    file.write(json_obj)

print("Hi")
print("Learning git commit")

#new kid branch

gyugbiuhbiu

bhhdsksk