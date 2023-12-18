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

# 実施_年月日の文字列を日付型に変換
df['実施_年月日'] = pd.to_datetime(df["実施_年月日"], format='%Y-%m-%d')

# 実施_年月日の表示を「年月日」形式に変更
df['実施_年月日'] = df['実施_年月日'].dt.strftime('%Y年%m月%d日')

# 実施_件数の値を整数に変換して、文字列としてフォーマット
df['検査実施_件数'] = df['検査実施_件数'].apply(lambda x: f"{int(x):,}件" if pd.notnull(x) else "")

# 最初の57行だけ表示
print(df.head(56))
