import csv
import os  # 追加: ファイルの存在チェックのために os モジュールを追加

def main():
    #絶対パス
    #file_path = "/Users/satoso/aftercamp/01_python/Day3/my_trial/data/193301.csv"

    #相対パス
    file_path = "data/193301.csv"


    # ファイルが存在するかチェック
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    with open(file=file_path, mode="r", encoding="utf-8") as f:
        next(f)  # ヘッダー行をスキップ

        reader = csv.reader(f)
    
        rows_data = []
        for row in reader:
            rows_data.append(row)

    print(rows_data)

if __name__ == "__main__":
    main()

print(os.getcwd())
