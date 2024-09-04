import tvscreener as tvs
from tvscreener import CryptoField, TimeInterval
from tvscreener.filter import FilterOperator
from tvscreener import ExtraFilter
from tvscreener.field import Exchange, SubMarket, SymbolType

import os

print("ddddd");
ss = tvs.CryptoScreener()
ss.add_filter(CryptoField.EXPONENTIAL_MOVING_AVERAGE_10, FilterOperator.ABOVE_OR_EQUAL, 20)
ss.add_filter(CryptoField.EXPONENTIAL_MOVING_AVERAGE_20, FilterOperator.ABOVE_OR_EQUAL, 50)
ss.add_filter(CryptoField.EXCHANGE,  FilterOperator.IN_RANGE, [ Exchange.UPBIT])
ss.sort_by(CryptoField.HIGH,ascending=False)
ss.set_range(0, 100)
df = ss.get()
print(df)


result_filename = os.getenv("RESULT_FILENAME")


with open(result_filename, "w") as f:
    f.write(str(df))



#print(df); 

# ... returns a dataframe with 150 rows by default