import requests
from bs4 import BeautifulSoup
import json
import gradio as gr


# --------------------------------
# Extract article text
# --------------------------------
def extract_article_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (EducationalBot/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return f"Error fetching article: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted elements
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()

    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text(strip=True) for p in paragraphs)

    return text


# --------------------------------
# Simplify using Ollama
# --------------------------------
def simplify_with_ollama(text):
    if not text.strip():
        return "No article text found."

    prompt = f"""
Read the following news article and explain it
in very simple language so that a beginner or
school student can understand it.

{text[:7000]}
"""

    payload = {
        "model": "gemma:2b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json=payload
        )
        result = response.json()
    except Exception as e:
        return f"Ollama error: {e}"

    return result.get("response", "No explanation generated.")


# --------------------------------
# Main Processing Function
# --------------------------------
def process_url(url):
    article_text = extract_article_text(url)

    if article_text.startswith("Error"):
        return article_text

    simplified_text = simplify_with_ollama(article_text)
    return simplified_text


# --------------------------------
# Gradio Interface
# --------------------------------
interface = gr.Interface(
    fn=process_url,
    inputs=gr.Textbox(label="Enter News Article URL"),
    outputs=gr.Markdown(label="Simplified Summary"),
    title="News Article Simplifier (Ollama)",
    description="Enter a news article URL and get a simplified explanation."
)


if __name__ == "__main__":
    interface.launch(inbrowser=True)
