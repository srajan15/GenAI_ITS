# 📘 Study Notes: Context Window, Tokens & API Costs in LLMs

---

## 🔹 1. The Context Window (Very Important Constraint)

### 🔸 What Is the Context Window?

- The **context window** is:
  - The **maximum number of tokens** a model can consider at one time

- It defines:
  - How much text the model can **remember**
  - How much input it can **process**

📌 If you exceed the context window → **the model fails**

---

### 🔸 What Counts Toward the Context Window?

The context window includes **everything**, not just your last message:

- System prompt
- Entire conversation history
- User messages
- Assistant replies
- Generated tokens (except the final token)

👉 **All of this must fit together**

---

## 🔄 2. Why the Context Window Fills Up So Fast

### 🔹 How Token Generation Works

- LLMs generate text **one token at a time**
- Each step:
  1. Full input sequence is passed in
  2. Model predicts the next token
  3. That token is appended to the input
  4. Process repeats

📌 So the context keeps growing continuously.

---

### 🔹 Example

Conversation like:

- “Hi, my name is Ed”
- “Nice to meet you, Ed”
- “What’s my name?”

➡️ All previous messages must still fit in memory.

---

## 🧠 3. Why Context Window Size Matters

The context window controls:

- How much **background** the model remembers
- How many **references** it can track
- How well it understands **long tasks**

📌 Bigger window = better long-form reasoning.

---

## 🧪 4. Context Window & Inference Techniques

### 🔹 Multi-shot Prompting

- Provide multiple **example Q&A pairs**
- Helps the model learn the pattern
- Requires **more tokens**

---

### 🔹 RAG (Retrieval-Augmented Generation)

- Injects documents into the prompt
- Uses context window heavily
- Larger window = more documents can be included

📌 Most inference-time scaling techniques depend on context size.

---

## 📚 5. Extreme Example: Shakespeare

- Complete works of Shakespeare:
  - ~1 million tokens

- Only models like **Gemini** can handle this today

📌 Context window limits what tasks are even possible.

---

## 💰 6. Chat Products vs API Costs

### 🔹 Chat Products (e.g., ChatGPT)

- Subscription-based:
  - Free tier
  - Paid tiers ($20–$200/month)

- No per-message billing
- Has rate limits

---

### 🔹 API Usage (Important)

- API usage is **pay-per-use**
- Subscription does **not** affect API costs
- Designed for:
  - Building your own products
  - Scaling to users

📌 APIs bill for **compute**, not convenience.

---

## 💸 7. How API Costs Are Calculated

API cost depends on:

- **Input tokens**
- **Output tokens**

---

### 🔹 Catch #1: Input Tokens Include Everything

You pay for:

- Full conversation history
- System prompts
- Memory
- RAG documents

📌 You _can_ send only the latest message, but:

- Quality drops badly

---

### 🔹 Catch #2: Reasoning Tokens Cost Money

- Reasoning models generate:
  - Hidden “thinking” tokens

- You:
  - Don’t see them
  - Still pay for them

📌 Compute still happens → cost still applies.

---

## ⚠️ 8. Cost Predictability Challenge

- Reasoning models:
  - Can vary in how much they think

- This leads to:
  - Slight unpredictability in cost

- But:
  - Necessary for better answers

---

## 📊 9. Understanding Costs with Real Numbers

### 🔹 Example: GPT-5 (Full Model)

- Context window: **400,000 tokens**
- Input cost: **$1.25 / million tokens**
- Output cost: **$10 / million tokens**

📌 $10 sounds high, but:

- That’s **1 million tokens**
- That’s an enormous amount of text

---

### 🔹 GPT-5 Nano (Tiny Model)

- Input: **$0.05 / million tokens**
- Output: **$0.40 / million tokens**

📌 Generating Shakespeare would cost **less than $1**

---

## 🧮 10. Cost Perspective (Very Important)

- Small experiments:
  - Cost is **almost nothing**

- “Hi, my name is Ed”:
  - Costs fractions of a cent

- Cost only matters when:
  - You scale
  - You use agent loops
  - You process large documents

---

## 🧠 11. Caching (Cost Optimization)

### 🔹 What Is Caching?

- If you send the **same input repeatedly**:
  - Cost can be reduced

- Works automatically in some systems

📌 Helpful for:

- Repeated prompts
- Large system prompts

---

## 📈 12. Comparing Context Windows (Key Models)

| Model                | Context Window |
| -------------------- | -------------- |
| **GPT-5**            | 400K tokens    |
| **Claude**           | 200K tokens    |
| **GPT-OSS**          | ~130K tokens   |
| **Gemini 2.5 Flash** | **1M tokens**  |

📌 Gemini currently leads in context size.

---

## 🧩 13. Why This Foundation Matters

At this point, you understand:

- Tokens
- Context windows
- API costs
- Transformer basics

This sets you up for:

- One-shot prompting
- Streaming responses
- JSON & Markdown outputs
- Real business solutions

---

## ⚡ Quick Revision (Must Remember)

- **Context window** = model memory limit
- Includes _entire conversation + generated tokens_
- Bigger window → better long-context tasks
- APIs charge per **input + output tokens**
- Reasoning tokens cost money (even if hidden)
- Chat subscriptions ≠ API pricing
- Small experiments are very cheap
- Scaling systems require cost planning
