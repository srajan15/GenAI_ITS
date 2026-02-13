import requests
from bs4 import BeautifulSoup

header = {
    "user-agent" :
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
  }

def fetch_website_content(url):

  response = requests.get(url, headers = header, timeout=20)
  soup = BeautifulSoup(response.text, "html.parser")

  title = soup.title.text if soup.title else "No title"

  for tag in soup(["script", "noscript", "style", "img", "footer"]):
    tag.decompose()

  if(soup.body):
    text = soup.body.get_text(separator="\n", strip=True)

  return (title + "\n\n" + text)[:2000]

print(fetch_website_content("https://www.imdb.com"))

def fetch_website_links(url):
  response = requests.get(url, headers=header, timeout=20)
  soup = BeautifulSoup(response.text, "html.parser")

  anchor_ele = soup.find_all("a")

  links = [link.get("href") for link in anchor_ele]

  return links
