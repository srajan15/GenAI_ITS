import requests
from bs4 import BeautifulSoup
import json


# -------------------------------
# Extract article text
# -------------------------------
def extract_article_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (EducationalBot/1.0)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted elements
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    paragraphs = soup.find_all("p")
    print(paragraphs)
    text = "\n".join(p.get_text(strip=True) for p in paragraphs)
    return text


    


# -------------------------------
# Simplify using Ollama
# -------------------------------
def simplify_with_ollama(text):
    prompt = f"""
Read the following news article and explain it
in very simple language so that a beginner or
school student can understand it.

{text[:7000]}
"""

    payload = {
        "model": "gemma3:270m",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        "http://localhost:11434/api/generate",
        json=payload
    )

    result = response.json()

    # Save full response
    with open("news_output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    return result.get("response", "No explanation generated.")




url = input("Enter news article URL: ")
print("\nExtracting article...\n")
article_text = extract_article_text(url)
print(article_text)

print("Simplifying article using Ollama...\n")
simplified_text = simplify_with_ollama(article_text)

print("------ SIMPLIFIED ARTICLE ------\n")
print(simplified_text)
