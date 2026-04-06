import pandas as pd
import requests
import xml.etree.ElementTree as ET

url = "https://feeds.feedburner.com/50WordStories"
resp = requests.get(url)

root = ET.fromstring(resp.content)

items = []

for item in root.findall(".//item"):
    data = {}
    for child in item:
        tag = child.tag.split("}")[-1]

        if tag in ["guid", "title", "pubDate", "description", "link"]:
            data[tag] = child.text

    items.append(data)

df = pd.DataFrame(items)
df.to_csv("topnews.csv", index=False)

print("Saved to topnews.csv")
