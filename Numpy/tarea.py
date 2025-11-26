
#
# Libreria Numpy
#
import numpy as np


a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])
c = np.zeros([5,5])
d = np.ones(5)
e = np.arange(0,10,2)
f = np.linspace(0,2,5)
g = np.eye(5)
h = np.random.rand(5)
i = a+d
j = g*7

#
# Libreria Pandas
#
import pandas as pd

serie1 = pd.Series([1,2,3])
serie1.name= "Primero"

serie2 = pd.DataFrame({"Columna1":[3,2,5,4,1], "columna2":["a","b","c","d","e"], "columna3":["?","!","#","@","&"]})


df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# print(df2.shape)
# print(df2.head())
# print(df2.size)
# print(df2.tail())

df2.columns=["largo_sepalo","ancho_sepalo","largo_petalo","ancho_petalo","especie"]
# print(df2.head())
df2["ancho_petalo"].value_counts()
# print(df2.dtypes)

# print(df2.memory_usage().sum())
# print(df2.T.head())
# print(df2.sort_values("especie", ascending=False))
# print(df2.especie)
# print(df2.iloc[[1,4],[1,2]])
# print(df2.isna().sum())

