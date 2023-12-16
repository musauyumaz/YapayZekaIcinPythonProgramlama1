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

# %% filtering

filtre1 = dataframe1.MAAS > 200

filtrelenmis_data = dataframe1[filtre1]

filtre2 = dataframe1.AGE < 20

dataframe1[filtre1 & filtre2]

dataframe1[dataframe1.AGE > 60]

# %% list comprehension
import numpy as np
ortalama_maas = dataframe1.maas.mean()

ortalama_maas_np = np.mean(dataframe1.maas)

dataframe1["maas_seviyesi"] = ["düşük" if ortalama_maas > i else "yüksek" for i in dataframe1.maas]

dataframe1.columns = [i.lower() for i in dataframe1.columns]

dataframe1.columns = [i.split()[0] + "_" + i.split()[1] if len(i.split()) > 1 else i for i in dataframe1.columns]


# %% drop and concatenating

# dataframe1.drop(["yeni_feature"],axis=1, inplace=True)

data1 = dataframe1.head()
data2 = dataframe1.tail()

# vertical
data_concat = pd.concat([data1,data2], axis = 0)


maas = dataframe1.maas
age = dataframe1.age


data_h_concat = pd.concat([maas,age], axis=1)

# %% transforming data 

dataframe1["list_comp"] = [ i * 2 for i in dataframe1.age]

# apply

def multiply(age):
    return age * 2

dataframe1["apply_metodu"] = dataframe1.age.apply(multiply)



