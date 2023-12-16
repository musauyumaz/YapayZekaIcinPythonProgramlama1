# %% pandas

import pandas as pd

dictionary = {"NAME" : ["ali","veli","kenan","gençay","hilal","ayşe"],
              "AGE" : [15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}

dataframe1 = pd.DataFrame(dictionary)

head = dataframe1.head()
tail = dataframe1.tail()