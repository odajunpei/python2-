import pandas as pd
import openpyxl

#csvファイルを読み込む
df = pd.read_csv("test.csv")

#ソート（国語の点数が高い順)
kokugo = df.sort_values("国語",ascending=False)

#Excelファイルに出力する。
kokugo.to_excel("csv_to_excel2.xlsx", index=False, sheet_name="国語でソート")
