import requests
import xml.etree.ElementTree as ET
import csv

def load_rss(url, xml_file):
    response = requests.get(url)
    with open(xml_file, "wb") as f:
        f.write(response.content)
    print("XML file saved successfully")

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    news_items = []

    for item in root.findall(".//item"):
        news = {
            "title": item.findtext("title"),
            "link": item.findtext("link"),
            "pubDate": item.findtext("pubDate"),
            "description": item.findtext("description")
        }
        news_items.append(news)

    return news_items

def save_to_csv(news_items, csv_file):
    fields = ["title", "link", "pubDate", "description"]

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(news_items)

    print("CSV file created successfully")

def main():
    rss_url = "https://feeds.feedburner.com/50WordStories"

    xml_file = "news.xml"
    csv_file = "news.csv"

    load_rss(rss_url, xml_file)

    items = parse_xml(xml_file)

    save_to_csv(items, csv_file)

if __name__ == "__main__":
    main()
