import os

import tvscreener as tvs
from tvscreener import CryptoField, ExtraFilter, TimeInterval
from tvscreener.field import Exchange, SubMarket, SymbolType
from tvscreener.filter import FilterOperator

print("ddddd");
ss = tvs.CryptoScreener()
ss.add_filter(CryptoField.EXPONENTIAL_MOVING_AVERAGE_10, FilterOperator.ABOVE_OR_EQUAL, 20)
ss.add_filter(CryptoField.EXPONENTIAL_MOVING_AVERAGE_20, FilterOperator.ABOVE_OR_EQUAL, 50)
ss.add_filter(CryptoField.EXCHANGE,  FilterOperator.IN_RANGE, [ Exchange.UPBIT])
ss.sort_by(CryptoField.HIGH,ascending=False)
ss.set_range(0, 100)
df = ss.get()
print(df)






#print(df); 

# ... returns a dataframe with 150 rows by default