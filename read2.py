import csv
import os


def main():
    #絶対パス
    #file_path = "/Users/satoso/aftercamp/01_python/Day3/my_trial/data/193301.csv"

    #相対パス
    file_path = "data/193301.csv"


    # ファイルが存在するかチェック
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    with open("data/193301.csv", mode="r", encoding="utf-8") as f:
        next(f)

        reader = csv.DictReader(f, fieldnames=["date", "code", "pre_name", "city_name", "test_count", "remarks", "pre_count"])
        rows_data = []
        for i, row in enumerate(reader):
            rows_data.append(row)
            if i + 1 == 56:
                break
            
        for row in rows_data:
            print(row)

if __name__ == "__main__":
    main()
