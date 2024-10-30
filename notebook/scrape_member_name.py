import json
from logging import getLogger
from pathlib import Path

from bs4 import BeautifulSoup

logger = getLogger(__name__)


def get_json_from_html(path: Path, output_name: str) -> None:
    # HTMLファイルを読み込む
    with open(path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(html_content, "html.parser")

    # 対象テーブルをクラス名で検索
    table = soup.find("table", {"class": "sortable wikitable jquery-tablesorter"})

    # ヘッダーを取得
    headers = [header.get_text(strip=True) for header in table.find_all("th")]

    # テーブルのデータを辞書として格納
    data = []
    for row in table.find_all("tr")[1:]:  # ヘッダー行をスキップ
        columns = row.find_all("td")
        if columns:
            row_data = {
                headers[i]: columns[i].get_text(strip=True) for i in range(len(columns))
            }
            data.append(row_data)

    # JSON形式に変換
    json_data = json.dumps(data, ensure_ascii=False, indent=2)

    # JSONをファイルに書き出し
    with open(f"json/{output_name}.json", "w", encoding="utf-8") as json_file:
        json_file.write(json_data)

    print(f"JSONファイル '{output_name}.json' に変換完了しました。")
