import json

from flask import Flask

from tradingview_screener import Query
from tradingview_screener.column import Column

app = Flask(__name__)

response = Query().select('close', 'volume', 'EMA5', 'EMA20', 'type').where(Column('close').between(Column('EMA5'), Column('EMA20')),Column('type')
       .isin(['stock'])).order_by('volume', ascending=False).get_scanner_data_raw()

@app.route('/')
def hello_world():
    return response['data']


@app.route('/array')
def send_array():
    return response['data']

data = response['data']

print(data)
