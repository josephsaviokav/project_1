import pandas as pd
k=pd.read_csv("data.csv")
k.dropna(inplace=True)
k.fillna(130,inplace=True)
print(k.to_string())

l=k["Calories"].mode()[0]
print(l)

