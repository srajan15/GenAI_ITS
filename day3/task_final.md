## Common Requirement (for all tasks)

```python
import requests
from bs4 import BeautifulSoup
```

---

## Task 1: Fetch Website Title

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Website Title:", soup.title.text)
```

---

## Task 2: Extract Paragraph Text

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

for p in paragraphs:
    print(p.text)
```

---

## Task 3: Count Hyperlinks

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")
print("Total hyperlinks:", len(links))
```

---

## Task 4: Extract Headings (h1, h2, h3)

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for tag in ["h1", "h2", "h3"]:
    headings = soup.find_all(tag)
    for h in headings:
        print(f"{tag.upper()}:", h.text)
```

---

## Task 5: Save Paragraphs to File (`content.txt`)

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

with open("content.txt", "w", encoding="utf-8") as file:
    for p in paragraphs:
        file.write(p.text + "\n")

print("Paragraphs saved to content.txt")
```

---

## Task 6: Extract Links with Text

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    text = link.text.strip()
    href = link.get("href")
    print(f"Text: {text} | URL: {href}")
```

---

## Task 7: Clean Readable Text Extraction

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for tag in soup(["script", "style", "noscript"]):
    tag.decompose()

clean_text = soup.get_text(separator="\n")
print(clean_text)
```

---

## Task 8: Count Common HTML Tags

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags = ["p", "a", "img", "h1", "h2"]

for tag in tags:
    count = len(soup.find_all(tag))
    print(f"{tag} tag count:", count)
```

---

## Task 9: Extract Image URLs (save to `images.txt`)

```python
url = input("Enter URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")

with open("images.txt", "w") as file:
    for img in images:
        src = img.get("src")
        if src:
            file.write(src + "\n")

print("Image URLs saved to images.txt")
```
