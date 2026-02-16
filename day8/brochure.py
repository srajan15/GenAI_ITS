from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urljoin
import google.generativeai as genai


# ----------------------------
# Configure Gemini
# ----------------------------

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash-lite")


headers = {
    "User-Agent": "Mozilla/5.0"
}


# ----------------------------
# Fetch Website Text
# ----------------------------

def fetch_website_contents(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return ""

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.text.strip() if soup.title else ""

    if soup.body:
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:2000]


# ----------------------------
# Fetch Website Links
# ----------------------------

def fetch_website_links(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    links = []
    for anchor in soup.find_all("a", href=True):
        absolute_url = urljoin(url, anchor["href"])
        if absolute_url.startswith("http"):
            links.append(absolute_url)

    return list(set(links))


# ----------------------------
# Filter Relevant Links (LLM)
# ----------------------------

def filter_relevant_links(links):

    prompt = f"""
You are an AI web content analyst.

Your task is to carefully evaluate a list of website URLs and select ONLY those URLs that contain meaningful company information suitable for generating a professional company sales brochure.

--------------------------------------------------
OBJECTIVE
--------------------------------------------------
From the given list of URLs, return ONLY the URLs that contain detailed company-related information that can help create a sales brochure.

--------------------------------------------------
INCLUDE URLs that likely contain:
--------------------------------------------------
- About Us / Company Overview pages
- Products or Services pages
- Solutions pages
- Industry or domain expertise pages
- Vision / Mission / Values pages
- Leadership or Team pages
- Company profile or brand story
- Case studies or client success stories
- Corporate information pages

--------------------------------------------------
EXCLUDE URLs that:
--------------------------------------------------
- Require login, authentication, or signup
- Are careers or job listings
- Are blog posts or news articles
- Are press releases (unless clearly company overview focused)
- Are contact-only pages
- Are legal pages (privacy policy, terms, cookies)
- Are dashboards or admin panels
- Are APIs
- Contain only forms or very little readable text
- Contain anchors (#) or mailto links
- Are social media links

--------------------------------------------------
IMPORTANT RULES
--------------------------------------------------
1. Return ONLY a valid json array.
2. Do NOT explain anything.
3. Do NOT add commentary.
4. Do NOT modify URLs.
5. Do NOT add extra text.
6. If no valid URLs exist, return an empty list: []
7. The output MUST be valid JSON-compatible Python list format.

--------------------------------------------------
INPUT URL LIST:
--------------------------------------------------
{links}

--------------------------------------------------
OUTPUT FORMAT (STRICTLY FOLLOW):
--------------------------------------------------
["https://example.com/about", "https://example.com/services"]

If no relevant links exist:
[]
"""

    response = model.generate_content(prompt)
    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()

    start = raw_text.find("[")
    end = raw_text.rfind("]")

    if start != -1 and end != -1:
        try:
            return json.loads(raw_text[start:end + 1])
        except json.JSONDecodeError:
            return []

    return []


# ----------------------------
# Collect Company Data
# ----------------------------

def collect_company_data(main_url, relevant_links):
    combined_text = fetch_website_contents(main_url)

    for link in relevant_links:
        combined_text += "\n\n" + fetch_website_contents(link)

    return combined_text[:6000]


# ----------------------------
# Generate Brochure
# ----------------------------

def generate_sales_brochure(company_data):

    prompt = f"""
Create a professional sales brochure using this information.

Include:
- Company overview
- Products / services
- Value proposition
- Target customers
- Why choose the company

Company data:
{company_data}
"""

    response = model.generate_content(prompt)
    return response.text


# ----------------------------
# Main
# ----------------------------

def main():
    company_url = "https://www.its.edu.in/"

    links = fetch_website_links(company_url)
    relevant_links = filter_relevant_links(links)

    company_data = collect_company_data(company_url, relevant_links)
    brochure = generate_sales_brochure(company_data)

    print(brochure)


if __name__ == "__main__":
    main()
