import requests
from bs4 import BeautifulSoup
import json

def summarize_with_ollama(text):
    prompt = f"""
Summarize the following website content in simple language:

{text[:8000]}
"""

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "gemma3:270m",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    print(response)

    result = response.json()
    print(result)

    with open("file.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    return result.get("response", "No summary generated")


def extract_website_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; EducationalSummarizer/1.0)"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())


# -------- MAIN --------
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
content = extract_website_text(url)
summary = summarize_with_ollama(content)

print("\n------ SUMMARY ------\n")
print(summary)
