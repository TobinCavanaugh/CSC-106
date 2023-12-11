import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

print(df)


print(df[["Age", "Fare"]].describe())