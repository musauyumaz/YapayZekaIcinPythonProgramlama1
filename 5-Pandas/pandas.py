# %% pandas

import pandas as pd

dictionary = {"NAME" : ["ali","veli","kenan","gençay","hilal","ayşe"],
              "AGE" : [15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}

dataframe1 = pd.DataFrame(dictionary)

head = dataframe1.head()
tail = dataframe1.tail()

# %% pandas basic method

print(dataframe1.columns)

print(dataframe1.info())

print(dataframe1.dtypes)

print(dataframe1.describe()) # numeric feature columns (age, maas)

# %% indexing and slicing

print(dataframe1["NAME"])
print(dataframe1["AGE"])
print(dataframe1.AGE)

dataframe1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataframe1.loc[:,"AGE"])

print(dataframe1.loc[:3,"AGE"])

print(dataframe1.loc[:3,["AGE","NAME"]])

print(dataframe1.loc[::-1,:])

print(dataframe1.loc[:, :"NAME"])

print(dataframe1.iloc[:, 2])
