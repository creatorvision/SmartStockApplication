"""
Organization : Smart Stockers
Appication : Stock Analytical Engine
Developer : Shivang Gupta 
Outcome of this script : Fetching the stock data.

"""
import requests

for i in range(10):
    stockSymbol = input()
    r= requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+stockSymbol+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")
    print (r.status_code)
    print (r.headers)
    print (r.content)