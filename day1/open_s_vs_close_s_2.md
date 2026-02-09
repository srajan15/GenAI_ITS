# 🎓 Slide 1: Open-Source AI Models – Big Picture

### Slide Content:

- AI models can be:
  - Closed source
  - Open source

- Today we focus on **open-source LLMs**

💡 _Open source = models anyone can use, study, and run_

---

# 🎯 Slide 2: Frontier vs Open-Source Models

### Slide Content:

- **Frontier models** usually mean:
  - Closed source
  - Built by companies like OpenAI, Anthropic

- **Open-source models**:
  - Code + weights available
  - Community-driven innovation

👉 Both are powerful, but used differently

---

# 🏆 Slide 3: Who Led Open-Source AI?

### Slide Content:

- **Meta** changed the game
- Open-sourced **LLaMA** models
- First big company to do this seriously

💡 This move made Meta a leader in open-source AI

---

# 🤔 Slide 4: Why Did Meta Open-Source LLaMA?

### Slide Content:

Possible reasons:

- Couldn’t compete with OpenAI headlines
- Wanted to stand out differently
- Took a strong stance:
  👉 _AI should be open_

📌 Result: Massive community adoption

---

# 🦙 Slide 5: LLaMA Models Overview

### Slide Content:

- LLaMA = Meta’s open-source LLM family
- Widely used in industry & research
- Core model we’ll use in this course

💡 _LLaMA is the backbone of many AI tools_

---

# 🔹 Slide 6: LLaMA 3.2 – Small but Powerful

### Slide Content:

- LLaMA 3.2 ≈ **3 billion parameters**
- Can run on:
  - Local computers

- Sometimes called:
  - **SLM** (Small Language Model)

👉 Still very powerful despite being “small”

---

# 📈 Slide 7: Small vs Large LLaMA Models

### Slide Content:

- Small models:
  - Easy to run locally
  - Fast

- Large models:
  - More intelligent
  - Need more hardware

💡 Bigger ≠ always better for learning

---

# 🇫🇷 Slide 8: Mistral – The French Innovator

### Slide Content:

- Company: **Mistral**
- Model type: **Mixture of Experts**
- Uses:
  - Multiple small specialist models

- Routes questions to best expert

🧠 _Like a team of specialists, not one brain_

---

# 🇨🇳 Slide 9: Qwen (Alibaba Cloud)

### Slide Content:

- Built by **Alibaba Cloud**
- Powerful but less popular
- Very strong performance

👉 Highly recommended to try

💡 Hidden gem in open-source AI

---

# 🔍 Slide 10: Gemma – Google’s Open Model

### Slide Content:

- **Gemma** = Open-source cousin of Gemini
- Comes in many sizes
- Smallest version:
  - **270 million parameters**

👉 Tiny but still talks and reasons

---

# 🧪 Slide 11: Why Gemma Is Impressive

### Slide Content:

- Very small model
- Still:
  - Understands text
  - Generates language

- Great for:
  - Learning
  - Experiments

💡 Shows how efficient modern AI is

---

# 🪟 Slide 12: Phi Models – Microsoft

### Slide Content:

- Microsoft’s open-source models
- Latest: **Phi-4**
- Strengths:
  - Tool calling
  - Business & commercial tasks

👉 Very practical models

---

# 🌊 Slide 13: DeepSeek – Why the World Was Shocked

### Slide Content:

- Built by **DeepSeek AI**
- Not the most powerful model
- BUT:
  - Extremely cheap to train

💡 Efficiency > raw power

---

# 💰 Slide 14: DeepSeek Cost Comparison

### Slide Content:

- GPT training cost:
  - ~$100M+

- DeepSeek training cost:
  - ~$4M

👉 Same level of capability
👉 Much lower cost

🔥 Huge breakthrough

---

# 📦 Slide 15: DeepSeek Model Sizes

### Slide Content:

- Main model:
  - **671B parameters**
  - Too big for local machines

- Smaller versions:
  - Can run locally

💡 How did they do that?

---

# 🧪 Slide 16: Distillation (Very Important Concept)

### Slide Content:

- Big model generates **synthetic data**
- Smaller models learn from it
- This process is called:
  👉 **Distillation**

🧠 Big brain teaches small brains

---

# 🆓 Slide 17: Why DeepSeek Matters

### Slide Content:

- Open-sourced
- Efficient
- Inspired others to open-source

👉 Changed AI ecosystem

---

# 🔓 Slide 18: OpenAI’s Open-Source GPT

### Slide Content:

- OpenAI released:
  - **GPT-OS**

- Two sizes:
  - Smaller (used in course)
  - Very large (needs huge hardware)

💡 Big surprise from OpenAI

---

# 🤯 Slide 19: Why Did OpenAI Do This?

### Slide Content:

Possible reason:

- Pressure from DeepSeek
- Open-source competition rising

👉 Open-source is winning attention

---

# 🧩 Slide 20: Three Ways to Use AI Models

### Slide Content:

1️⃣ Products (ChatGPT)
2️⃣ Cloud APIs
3️⃣ Run models yourself

👉 We will use **all three**

---

# 🧠 Slide 21: Using AI as a Product

### Slide Content:

- Example:
  - ChatGPT

- Includes:
  - UI
  - Memory
  - Tools
  - Web search

👉 You’re using a **product**, not just a model

---

# ☁️ Slide 22: Using AI via Cloud APIs

### Slide Content:

- Call models using APIs
- Examples:
  - OpenAI API
  - Amazon Bedrock
  - Google Vertex AI
  - Azure ML

👉 Managed & scalable

---

# 🧪 Slide 23: Special Platforms

### Slide Content:

- Groq (with Q)
- OpenRouter
- Fast cloud inference
- Model routing

⚠️ Groq ≠ Elon Musk’s Grok

---

# 🖥️ Slide 24: Running Models Yourself (Inference)

### Slide Content:

- Download model
- Run locally
- No cloud
- Full control

👉 This is **real AI engineering**

---

# 🧠 Slide 25: What Is Inference?

### Slide Content:

> **Inference = Running a trained model on new input**

Example:

- Input → Question
- Output → Answer

📌 Fancy word, simple meaning

---

# 🧰 Slide 26: Two Ways to Run Open-Source Models

### Slide Content:

1️⃣ Hugging Face Transformers
2️⃣ Ollama

👉 Same goal, different approach

---

# 🐍 Slide 27: Hugging Face Transformers

### Slide Content:

- Python-based
- Full control
- Run model code yourself
- Uses model weights directly

👉 Flexible but complex

---

# ⚡ Slide 28: What Is Ollama?

### Slide Content:

- Packaged product
- Optimized C++
- Compressed model files
- Easy to run

👉 Fast + beginner-friendly

---

# 🔄 Slide 29: Hugging Face vs Ollama

### Slide Content:

| Hugging Face | Ollama       |
| ------------ | ------------ |
| Flexible     | Simple       |
| Python code  | Ready-made   |
| More control | Faster setup |

---

# ⭐ Slide 30: Final Teaching Takeaway

### Slide Content:

🧠 **Open-source AI gives you power**

- You can:
  - Study models
  - Run them
  - Build products

- This course teaches:
  👉 _Real AI engineering_

---
