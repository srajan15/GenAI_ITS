# 📘 Revision Notes: Getting Started with LLMs (Hands-on First Approach)

## 1️⃣ Course Mindset: _Action First, Theory Later_

- This course **does NOT start with long theory or syllabus explanations**

💡 _Key idea_:

> Don’t wait to understand everything. Start using LLMs first, understanding will follow.

---

## 2️⃣ What Is an LLM? (Quick Recall)

- **LLM (Large Language Model)** = AI model trained on massive text data
- Examples you already know:
  - ChatGPT
  - Claude
  - Gemini

- Difference here 👉 **We will run LLMs on our own computer (locally)**

---

## 3️⃣ Why Run LLMs Locally?

Running LLMs on your own machine means:

- 🔒 More privacy (no cloud)
- ⚙️ Full control
- 🧠 Better understanding of how LLMs actually work
- 👨‍💻 Real **LLM Engineering** experience (not just chatting)

💡 This is a BIG step from “AI user” → “AI engineer”

---

## 4️⃣ Course Repository (GitHub)

- The course has a **GitHub repository**
- Important file: **README**
- README contains:
  - Setup instructions
  - Links
  - Updates (always latest info)
  - “Instant Gratification” section

📌 **Always check README first** – it’s the source of truth.

---

## 5️⃣ Tool Used: Ollama (Very Important)

### What is Ollama?

- Ollama lets you:
  - Download open-source LLMs
  - Run them **locally**
  - Interact via terminal/command line

### Key Points:

- Works on:
  - Windows
  - macOS
  - Linux

- Fast, optimized, beginner-friendly
- Inspired by Meta’s LLaMA models

💡 Think of Ollama as:

> “Docker for LLMs”

---

## 6️⃣ Installing & Running Ollama (Conceptual Flow)

1. Download Ollama for your OS
2. Install it normally
3. Launch Ollama (it runs in background)
4. Close its UI (we won’t use chat UI)
5. Open:
   - **Terminal** (Mac/Linux)
   - **PowerShell** (Windows)

6. Type:
   - `ollama` → to check it’s working
   - `ollama serve` → confirms it’s running

---

## 7️⃣ Running Your First Local LLM (Gemma)

### Model Used:

- **Gemma 3 (270M parameters)**
- Created by Google
- Very small model (for demo)

### Command:

```bash
ollama run gemma:270m
```

### What happens?

- Model downloads from internet
- Starts running locally
- You can chat with it directly in terminal

📌 **Parameter meaning (intro level)**:

- Parameters = brain size of the model
- 270M = very small
- Modern models usually have **billions**

---

## 8️⃣ Expectations from Small Models

- Responses are basic
- Not very intelligent
- But still impressive because:
  - 🧠 It’s running on _your own machine_

💡 Learning goal:

> Understand limitations vs size

---

## 9️⃣ Trying Bigger Models (Model Comparison)

After exiting Gemma (`Ctrl + D`), explore more models.

### Example 1: Phi-3 (Microsoft)

- Size: ~2.2GB
- Much smarter than Gemma
- Better conversations

```bash
ollama run phi3
```

💡 Bigger model = better reasoning (generally)

---

### Example 2: Very Large Model (Advanced)

- Open-source GPT-style model
- ~20 billion parameters
- Requires:
  - ~16GB RAM
  - ~20GB disk space

📌 **Optional** – only for powerful machines

Learning purpose:

- Feel the difference between:
  - Small LLM
  - Medium LLM
  - Large LLM

---

## 🔁 How to Stop a Model

- Press:

```bash
Ctrl + D
```

- Ends the current model session

⚠️ Note:

- **Ctrl ≠ Command (Mac users)**

---

## 🔑 Key Takeaways (Exam / Interview Ready)

- LLMs can run **locally**, not just in cloud
- Ollama makes local LLM execution easy
- Model size (parameters) matters a LOT
- Bigger models = better responses but more resources
- LLM Engineering starts with **hands-on usage**

---

## 🧠 Big Picture (Why This Matters for AI Engineers)

This lesson sets foundation for:

- LLM Engineering
- RAG systems
- Fine-tuning (QLoRA)
- AI Agents

Because:

> You can’t engineer what you’ve never run yourself.

---

Let’s do **“parameters”** in the **easiest, friendliest way possible** — perfect for revision + teaching + interviews.

---

# 🧠 What Are _Parameters_ in an LLM? (Super Easy Analogy)

## First: One-Line Meaning

**Parameters are the memory + knowledge stored inside an AI model.**

> More parameters = more things the AI can remember and connect.

---

## 🍔 Analogy 1: AI Brain = Human Brain

- **Your brain neurons** → help you remember, think, decide
- **LLM parameters** → do the same for AI

👉 **Parameters = AI’s neurons**

| Human        | AI               |
| ------------ | ---------------- |
| Neurons      | Parameters       |
| Experience   | Training data    |
| Intelligence | Model capability |

---

## 🧳 Analogy 2: Suitcase Size

Imagine AI is traveling.

- **270M parameters (Gemma small)**
  🧳 Small bag → only basics fit
  - Simple answers
  - Weak reasoning

- **2B parameters (Phi-3)**
  🧳 Medium suitcase
  - Better facts
  - Decent conversation

- **20B+ parameters (Big models)**
  🧳 Huge suitcase
  - Deep knowledge
  - Better logic
  - Context awareness

👉 Bigger suitcase = more things AI can carry

---

## 📚 Analogy 3: Student Level

Think of parameters as **education level**:

- **Few parameters** → School student
- **More parameters** → College student
- **Many parameters** → PhD researcher

💡 A PhD can answer deeper questions because they **stored more knowledge and patterns**

---

## 🔢 What Exactly Is a Parameter? (Simple Technical Meaning)

- A parameter is **a number**
- That number tells the model:
  - Which word is likely next
  - How words relate to each other
  - What tone to use
  - What facts connect together

👉 **Millions/Billions of tiny numbers working together**

---

## 🤖 Why Small Models Feel “Dumb”

Example:

```text
Gemma 270M
```

- Very few parameters
- Limited patterns learned
- Short memory
- Weak reasoning

So it may:

- Give basic answers
- Miss context
- Make more mistakes

⚠️ **Not broken — just small brain**

---

## 🚀 Why Big Models Feel “Smart”

Example:

```text
GPT-style 20B+
```

- Huge number of parameters
- Learns complex patterns
- Understands context better
- Gives structured answers

👉 That’s why ChatGPT feels human-like

---

## 🖥️ Parameters vs Computer Power (Important)

More parameters = more resources needed

| Parameter Size | Needs              |
| -------------- | ------------------ |
| Small (M)      | Low RAM, fast      |
| Medium (B)     | Moderate RAM       |
| Large (10B+)   | High RAM + storage |

💡 That’s why:

- Small models run easily on laptops
- Big models need strong machines / cloud

---

## 🎯 Interview-Ready Answer (Short)

> **Parameters are internal numerical values that store knowledge and relationships in an AI model. More parameters generally allow the model to understand language better, reason deeper, and produce higher-quality responses.**

---

## ⭐ Final Memory Trick

🧠 **Parameters = AI’s brain size**

Say this in your head:

> _“More parameters, more thinking power — but more hardware needed.”_

---
