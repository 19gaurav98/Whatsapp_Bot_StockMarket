import os
import requests
import json

os.environ['MARKETSTACK_KEY'] ='7839e4e51b673e6922c83fa97d4decba'

API_KEY=os.environ.get("MARKETSTACK_KEY")
BASE_URL='http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params={
        'access_key': API_KEY

    }
    end_point = ''.join([BASE_URL,"tickers/" , stock_symbol ,'/intraday/latest'])
    api_result = requests.get(end_point, params)
   # api_result=requests.get('http://api.marketstack.com/v1/tickers/AAPL/intraday/latest?access_key=7839e4e51b673e6922c83fa97d4decba')
    print(api_result)
    json_result=json.loads(api_result.text)
    
    return{
        "open":json_result["open"]
    }

    #  p="http://api.marketstack.com/v1/intraday?access_key=7839e4e51b673e6922c83fa97d4decba&symbols=AAPL"




# result = get_stock_price("AAPL")
# print(result)


# import requests

# params = {
#   'access_key': '7839e4e51b673e6922c83fa97d4decba'
# }

# api_result = requests.get('http://api.marketstack.com/v1/tickers/aapl/eod', params)

# api_response = api_result.json()

# for stock_data in api_response['data']:
#     print(u'Ticker %s has a day high of  %s on %s' % (
#       stock_data['symbol'],
#       stock_data['high'],
#       stock_data['date']
#     ))
