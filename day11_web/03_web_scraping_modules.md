# Libraries

## Requests Module

It is a library used for making HTTP requests to a specific URL and returns the response. Python requests provide inbuilt in functinalities for managing both the reuqest and response.
It is installed using `pip install requests`
Example: Making a request:

```python
from bs4 import BeautifulSoup

r = requests.get("https://www.geeksforgeeks.org/python-web-scraping-tutorial/")

print(r.content)
```

## Beautifulsoup4

It is a module that provides a few simple methods ant pythonic pharses for guiding, searching, and changing a parse tree: a toolkit for studying a document and removing what you need.
Example:

```python
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.geeksforgeeks.org/python-web-scraping-tutorial/")

soup = BeautifulSoup(r.content, "html.parser")

s = soup.find("div", class_="text")
content = soup.find_all("p")
print(content)
```

## Lxml

It is a powerful library for processing XML and HTML documents. It provides a high-performance XML and HTML parsing capabilities along with a simple and Pythonic API.
