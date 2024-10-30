from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_html(url, out_dir: Path, out_file: str) -> Path:
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the member table by its class or id
    member_table = soup.find("table", {"class": "wikitable"})

    # Save the HTML content of the table to a file
    out_path = out_dir / (out_file + ".html")
    with open(out_path, "w") as f:
        f.write(str(member_table))

    return out_path
