import json
from pathlib import Path

from bs4 import BeautifulSoup


def html_to_json(html_path: Path, out_dir: Path, out_file: str) -> None:
    # HTMLファイルを読み込む
    with open(html_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    member_table = soup.find("table", {"class": "wikitable"})

    # Extract table headers
    headers = [header.text.strip() for header in member_table.find_all("th")]

    # Extract table rows
    rows = []
    for row in member_table.find_all("tr")[1:]:  # Skip the header row
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        rows.append(dict(zip(headers, row_data)))

    # Convert to JSON
    json_data = json.dumps(rows, ensure_ascii=False, indent=4)

    # Save JSON to a file
    out_path = out_dir / (out_file + ".json")
    with open(out_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_data)

    print(f"JSON data has been saved to {out_path}")
