import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

USERNAME = "bathlaparth036-max"

url = f"https://github.com/users/{USERNAME}/contributions"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

days = []

for tag in soup.select("td.ContributionCalendar-day"):
    date = tag.get("data-date")
    level = tag.get("data-level", "0")

    if date:
        days.append({
            "date": date,
            "level": int(level)
        })

data = {
    "username": USERNAME,
    "updated": datetime.now().isoformat(),
    "days": days
}

with open("data/contributions.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Fetched {len(days)} contribution days successfully!")