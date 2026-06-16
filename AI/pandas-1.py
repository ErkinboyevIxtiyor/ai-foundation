import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford", "Chevrollet", "MERS", "AUDI"],
    'counts': [3, 7, 2, 5, 8, 7]
}

df = pd.DataFrame(mydataset)
print(df)

print("=================\n")

dfHead = df.head()  # limit default 5 row
print(dfHead)

print("=================\n")

dfTail = df.tail()  # reverse limit default 5 rows
print(dfTail)

print("=================\n")
print("shape:", df.shape)

print("=================\n")
print("columns:", df.columns)

print("=================\n")
print("dtypes:", df.dtypes)

print("=================\n")
print("describe:", df.describe(include="all"))  # numerical columns only

print("=================\n")
print("iloc:", df.iloc[0])

print("=================\n")
print("loc:", df.loc[:, "cars"])

print("=================\n")
print("counts >3 ", df[df["counts"] > 3])

print("=================\n")
print("mean() ", df.mean(numeric_only=True))

print("=================\n")
print("df.sum()", df.sum())

print("=================\n")
print("df.median()", df.median(numeric_only=True))

print("=================\n")
print("df.count()", df.count())

print("=================\n")
print("df.std()", df.std(numeric_only=True))

data_with_missing = {
    "cars": ["BMW", "Volvo", None, "Tesla", "Ferrari", None, "Ford"],
    "counts": [3, 7, None, 8, 1, 9, None]
}
df_missing = pd.DataFrame(data_with_missing)

print("=================\n")
print("df_missing", df_missing)

print("=================\n")
print("isnull", df_missing.isnull().sum())

print("=================\n")
print("dropna", df_missing.dropna())

print("=================\n")
print("fillna", df_missing.fillna("unknown"))

df = pd.read_csv("Titanic-Dataset.csv")
print("titanic", df.head(100))

df.to_excel("output.xlsx")
