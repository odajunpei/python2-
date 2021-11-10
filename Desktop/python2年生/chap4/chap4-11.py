import pandas as pd

#データフレームを読み込む
df1 = pd.read_csv("最高気温.csv")
df2 = pd.read_csv("年平均気温.csv")
df3 = pd.read_csv("最低気温.csv")

print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)
