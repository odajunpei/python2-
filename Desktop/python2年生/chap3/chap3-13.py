import pandas as pd

#csvファイルを読み込む
df = pd.read_csv("test.csv")

#ソート(国語の点数が高いもの順)
kokugo = df.sort_values("国語",ascending=False)

#csvファイルに出力する（インデックスとヘッダーを削除)
kokugo.to_csv("export3.csv", index=False, header=False)
