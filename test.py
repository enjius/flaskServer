import json

from tradingview_screener import Query
from tradingview_screener.column import Column

response = Query().select('close', 'volume', 'EMA5', 'EMA20', 'type').where(Column('close').between(Column('EMA5'), Column('EMA20')),Column('type')
       .isin(['stock'])).order_by('volume', ascending=False).get_scanner_data_raw()



data = response['data']
          
print(data)           
