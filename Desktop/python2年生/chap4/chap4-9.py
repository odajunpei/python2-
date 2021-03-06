import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#データフレームを読み込む
df = pd.read_csv("FEH_00200524_211110105529.csv", index_col="全国・都道府県", encoding="shift_jis")

#2019ねんの列データを棒グラフで表示
df = df.drop("全国", axis=0)
df["2018年"] = pd.to_numeric(df["2018年"].str.replace(",", ""))
df["2019年"] = pd.to_numeric(df["2019年"].str.replace(",", ""))
df["人口増減"] = df["2019年"] - df["2018年"]
df = df.sort_values("人口増減", ascending=False)
df["人口増減"].plot.bar(figsize=(10,6))
plt.show()
                            
