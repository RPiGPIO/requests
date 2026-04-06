from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href":
                    self.links.append(value)

    def getLinks(self, url):
        self.links = []
        html = urlopen(url).read().decode("utf-8")
        self.feed(html)
        return html, self.links


def crawl(url, word):
    visited = []
    found = []
    count = 0

    parser = LinkParser()
    data, links = parser.getLinks(url)
    links.append(url)

    for link in links:
        if link not in visited:
            visited.append(link)
            count += 1

            try:
                data, new_links = parser.getLinks(link)
                print(count, "Visiting:", link)

                if word.lower() in data.lower():
                    print("Word found at:", link)
                    found.append(link)

            except:
                print("Failed:", link)

    print("\nTotal pages visited:", count)
    print("Found URLs:", found)


crawl("https://www.ruiacollege.edu", "computer")
