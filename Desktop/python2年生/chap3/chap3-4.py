import pandas as pd

#csvファイルを読み込む
df = pd.read_csv("test.csv")

#1行のデータを表示
print("c子のデータ\n",df.loc[2])

#複数行のデータを表示
print("C子とD郎のデータ\n",df.loc[[2,3]])

#指定した行の指定した列のデータを表示
print("C子の国語データ\n",df.loc[2]["国語"])
