import csv
from pathlib import Path

csv_path = Path(__file__).parent / "MOCK_DATA.csv"

with open(csv_path, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['first_name']} {row['last_name']}")
