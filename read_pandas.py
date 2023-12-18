import pandas as pd

df = pd.read_csv(
    "data/193301.csv",
    usecols=[0, 1, 2, 3, 4, 5, 6],
    delimiter=",",
    dtype={"実施_年月日": "str", "全国地方公共団体コード": "str", "都道府県名": "str", "市区町村名": "str", "実施_件数": "Int64", "備考": "str", "【参考】件数（県）": "Int64"},
    encoding="utf-8-sig",
    thousands=',',  # コンマを取り除く
    na_values=["-"],  # "-" を欠損値として扱う
)

df['実施_年月日'] = pd.to_datetime(df["実施_年月日"], format='%Y-%m-%d')

print(df)
