import pandas as pd

df = pd.read_csv(
    "data/193301.csv",
    usecols=[0, 4],
    delimiter=",",
    dtype={"実施_年月日": "str", "検査実施_件数": "float"},
    encoding="utf-8-sig",
    thousands=',',  # コンマを取り除く
    na_values=["-"],  # "-" を欠損値として扱う
)

df['実施_年月日'] = pd.to_datetime(df["実施_年月日"], format='%Y-%m-%d')



# 検査実施_件数列を数値に変換
df['検査実施_件数'] = pd.to_numeric(df['検査実施_件数'], errors='coerce')

# 検査実施_件数が2000以上の行だけ表示
filtered_df = df[df["検査実施_件数"] >= 2000]
filtered_df['検査実施_件数'] = filtered_df['検査実施_件数'].apply(lambda x: f"{int(x)}件")

print(filtered_df)
