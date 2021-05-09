from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os

app = Flask(__name__)

os.environ['TwILIO_ACCOUNT'] ='AC24ad229e790e5b46abeab20fd75c5256'
os.environ['TWILIO_TOKEN'] ='a599880d5362d577da392b8081ac5ff7'

ACCOUNT_ID=os.environ.get('TWILIO_ACCOUNT')
print(ACCOUNT_ID)
TWILIO_TOKEN=os.environ.get('TWILIO_TOKEN')
client=Client(ACCOUNT_ID,TWILIO_TOKEN)
TWILIO_NUMBER='whatsapp:+14155238886'

def process_msg(msgs):
    response = ""
    if msgs == "hi":
        response ="Hello, Welcome to the stock market bot" + "Type sym:<stock_symbol> to know the price of the stock"
       # response +="Type sym:<stock_symbol> to know the price of the stock"
    elif 'sym:' in msgs:
        data=msgs.split(":")
        stock_symbol=data[1]
        stock_price=get_stock_price(stock_symbol)
        last_price=stock_price['open']
        last_price_str=str(last_price*73.25)
        response="The Stock Price of "+stock_symbol+" is : Rs "+last_price_str

    else:
        response="Please Type Hi to get started"
    return response 

def send_msg(msg,recipient):
    try:
        client.messages.create(
            from_=TWILIO_NUMBER,
            body=msg,
            to=recipient
            )
    except TwilioRestException as ex:
        print(ex)

@app.route("/webhook",methods=["POST"])
def webhook():
    f=request.form
    msg = f['Body']
    sender = f['From'] 
    response=process_msg(msg)
    print(response)
    send_msg(response,sender)
    return "OK",200






if __name__ == "__main__":
    app.run()

#AC24ad229e790e5b46abeab20fd75c5256
#a599880d5362d577da392b8081ac5ff7
#7839e4e51b673e6922c83fa97d4decba
