# matplotlib gorsellestirme kutuphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)
print(df.Species.unique())

print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

# %% 
import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)

# df1.plot()
# plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red", label = "setosa", grid = True)
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm, color = "blue", label = "virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid=True, linestyle = ":")
df1.plot(grid=True, alpha = 0.1)
plt.show()

# %% scatter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red", label="setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color="green", label="versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color="blue", label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.xlabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()


