import requests
from bs4 import BeautifulSoup
import json
import gradio as gr


# --------------------------------
# Extract Website Text
# --------------------------------
def extract_website_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; EducationalSummarizer/1.0)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return f"Error fetching website: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted elements
    for tag in soup(["script", "style", "noscript", "img"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    cleaned_text = " ".join(text.split())

    return cleaned_text


# --------------------------------
# Summarize using Ollama
# --------------------------------
def summarize_with_ollama(text):

    if not text.strip():
        return "No content found to summarize."

    prompt = f"""
Summarize the following website content in simple and clear language:
do content as list

{text[:8000]}
"""

    payload = {
        "model": "gemma3:270m",
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

    return result.get("response", "No summary generated.")


# --------------------------------
# Main Function for Gradio
# --------------------------------
def process_url(url):
    content = extract_website_text(url)

    # If extraction failed
    if content.startswith("Error"):
        return content

    summary = summarize_with_ollama(content)
    return summary


# --------------------------------
# Gradio Interface
# --------------------------------
interface = gr.Interface(
    fn=process_url,
    inputs=gr.Textbox(label="Enter Website URL"),
    outputs=gr.Markdown(label="Website Summary"),
    title="Website Summarizer (Ollama)",
    description="Enter a website URL to generate a simple summary using a local Ollama model."
)


if __name__ == "__main__":
    interface.launch()
