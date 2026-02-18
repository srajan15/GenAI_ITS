import google.generativeai as genai
from scrapper import fetch_website_contents, fetch_website_links
import json
import requests

genai.configure(api_key="api key")
gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi3"



def generate_with_llm(prompt, model_choice):
    if model_choice == "Ollama (gemma3:270m)":
        return generate_with_ollama(prompt)
    else:
        return generate_with_gemini(prompt)

def generate_with_gemini(prompt):
    response = gemini_model.generate_content(prompt)
    return response.text

def generate_with_ollama(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        print("Ollama error:", response.text)
        return ""

def filter_links(company_url, links, model_choice):
  links = links[:25]
  prompt = f"""
  help me to analyze a company website here is the website url
  {company_url} which have differnt links {links}
  filter links that are relvant to brochure such as company services and about company etc 
  strict rules:
   - Return ONLY valid JSON. 
   - Do not include markdown.
   - Do not include explanation.
   - Do not include backticks.

  Examples:
  ["https://www.company_name/service.com", "https://www.company_name/about.com"]
"""
  res = generate_with_llm(prompt, model_choice)
  raw_text = res.strip()

  if raw_text.startswith("```"):
    raw_text = raw_text.replace("```json", "").replace("```", "").strip()


  try:
      return json.loads(raw_text)
      
  except:
      return []



def collect_company_data(main_url, relevant_links):
    """
    Collects text from:
    - Main website
    - All AI-selected relevant pages
    """

    combined_text = fetch_website_contents(main_url)

    for link in relevant_links:
        try:
            combined_text += "\n\n" + fetch_website_contents(link)
        except Exception:
            pass

    return combined_text[:6_000]


# ======================================================
# STEP 4 – Generate Sales Brochure (LLM Call #2)
# ======================================================

def generate_sales_brochure(company_data, model_choice):

    """
    Generates a professional sales brochure.
    """

    prompt = f"""
You are a professional marketing copywriter.

Using the information below, create a clear and
persuasive sales brochure for potential clients
or investors.

Include:
- Company overview
- Products / services
- Unique value proposition
- Target customers
- Why choose this company

Company information:
{company_data}
"""

    return generate_with_llm(prompt, model_choice)



# ======================================================
# STEP 5 – Orchestration (Main)
# ======================================================

def fetch_brochure(company_url, model_choice):

    print("Fetching links...")
    links = fetch_website_links(company_url)

    print("Filtering relevant links with Gemini...")
    relevant_links = filter_links(company_url, links, model_choice)

    print("Collecting company data...")
    company_data = collect_company_data(company_url, relevant_links)

    print("Generating sales brochure...\n")
    brochure = generate_sales_brochure(company_data, model_choice)

    print("========== SALES BROCHURE ==========\n")
    return brochure