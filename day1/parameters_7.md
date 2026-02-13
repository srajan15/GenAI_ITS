# 📘 Study Notes: Parameters, Model Size & Scaling in LLMs

---

## 🔹 1. Why “Parameters” Matter in LLMs

- You often hear statements like:
  - **LLaMA 3.2 → 8 billion parameters**
  - **Gemma (smallest) → 270 million parameters**

- Parameters are one of the **most important ideas** behind how powerful an LLM is

📌 Understanding parameters helps you understand:

- Model size
- Cost
- Capability
- Why models come in “nano / mini / large” versions

---

## 🧠 2. What Are Parameters?

### 🔸 Simple Definition

**Parameters** are the **learned numbers** inside a neural network that:

- Store information from training data
- Control how the model transforms input into output

👉 They are like the **knowledge storage** of the model.

---

### 🔸 Intuition

- Parameters decide:
  - Which words relate to each other
  - Which patterns matter
  - How strongly one concept influences another

📌 More parameters → more capacity to learn patterns.

---

## 🧮 3. Parameters in Traditional ML vs Deep Learning

### 🔹 Traditional Machine Learning

- Typical models used:
  - **20–200 parameters**

- Example:
  - Credit scoring model
  - Uses 20–30 factors (income, age, history)

---

### 🔹 Deep Neural Networks

- Parameters jumped dramatically
- Early deep models:
  - Millions of parameters

- Modern LLMs:
  - **Billions to trillions**

📌 This jump shocked early practitioners.

---

## 🚀 4. Parameter Explosion: GPT Timeline

| Model                      | Parameters                         |
| -------------------------- | ---------------------------------- |
| **GPT-1**                  | 117 million                        |
| **GPT-2**                  | 1.5 billion                        |
| **GPT-3**                  | 175 billion                        |
| **GPT-4**                  | ~1.76 trillion                     |
| **Latest frontier models** | Unknown (likely tens of trillions) |

📌 Labs no longer reveal exact counts.

---

## 📉 5. Doing More With Fewer Parameters

- Example:
  - **Gemma (270M)** > **GPT-2 (1.5B)** in capability

- Reason:
  - Better architectures
  - Better training methods
  - Better data efficiency

📌 **Efficiency has improved**, not just size.

---

## 🧠 6. General Rule (Important)

> **More parameters usually mean a more capable model**

Because:

- More parameters → more training data absorbed
- More representational capacity

⚠️ But:

- Architecture and training quality also matter

---

## 🧩 7. Why Models Come in Different Sizes

### Examples:

- **GPT-5**:
  - Nano
  - Mini
  - Full

- **Claude**:
  - Haiku (small)
  - Sonnet (medium)
  - Opus (large)

### Why this exists:

- Different parameter counts
- Different compute costs
- Different speed vs intelligence trade-offs

📌 Bigger models cost more to run.

---

## 💰 8. Parameters & Cost

- Cost comes from:
  - Computing trillions of parameters

- Larger model:
  - Higher API cost
  - Slower inference

- Smaller model:
  - Faster
  - Cheaper

📌 This is why pricing tiers exist.

---

## 📈 9. Training-Time Scaling

### 🔸 What Is Training-Time Scaling?

- Increasing:
  - Model size
  - Number of parameters

- Requires:
  - More compute
  - More money
  - More training data

📌 Bigger model → longer and more expensive training.

---

### 🔸 Chinchilla Scaling Laws (Background)

- Suggest:
  - Optimal relationship between:
    - Parameters
    - Training data size

- Rough idea:
  - Bigger models need proportionally more data

📌 Less discussed today, but foundational.

---

## ⚙️ 10. Inference-Time Scaling (Very Important)

### 🔸 What Is Inference?

- **Inference** = running a trained model
- Happens after training is complete

---

### 🔸 Inference-Time Scaling Techniques

#### 1️⃣ Reasoning Techniques

- Ask model to:
  - “Think step by step”

- Budget forcing:
  - Insert **“wait”**
  - Force deeper reasoning

📌 Improves output quality without retraining.

---

#### 2️⃣ More Context (Input Data)

- Provide:
  - Ticket prices
  - Policies
  - Documents

- Model draws from input sequence

📌 This leads directly to **RAG**.

---

## 🆚 11. Training-Time vs Inference-Time Scaling

| Aspect      | Training-Time Scaling | Inference-Time Scaling   |
| ----------- | --------------------- | ------------------------ |
| When        | During training       | While using model        |
| Method      | More parameters       | More reasoning / context |
| Cost        | Very high             | Much lower               |
| Flexibility | Fixed                 | Adjustable per query     |

📌 These are **orthogonal approaches** — you can use both.

---

## 📊 12. Logarithmic Scale of Model Sizes

### Important Note

- Parameter charts use **logarithmic scale**
- Each step = **10× increase**

📌 1B → 10B → 100B → 1T

---

## 🧪 13. Open-Source Model Sizes (Examples)

- **LLaMA 3.2** → 3B parameters
- **LLaMA 3.1** → 8B (stronger)
- **LLaMA 3.3** → 3.3B
- **LLaMA 4** → multimodal (~2.45B variant)
- **GPT-OSS**:
  - 20B
  - 120B

- **DeepSeek**:
  - 671B parameters

📌 Many large models use **Mixture of Experts (MoE)**.

---

## 🧠 14. Mixture of Experts (MoE)

### 🔸 What Is MoE?

- Model contains:
  - Many smaller sub-models

- Only some activate per query

📌 Efficient way to scale without using all parameters every time.

---

## 🤯 15. Take a Step Back: Scale Is Enormous

- Modern frontier models:
  - Likely **tens of trillions** of parameters

- This scale is:
  - Hard to imagine
  - Unprecedented in computing history

📌 This is why LLM behavior can feel magical.

---

## ⚡ Quick Revision (Must Remember)

- **Parameters** = learned numbers storing knowledge
- Traditional ML: tens of parameters
- LLMs: billions → trillions
- More parameters → more capacity (usually)
- Models come in sizes due to **cost vs capability**
- **Training-time scaling** = bigger model
- **Inference-time scaling** = better prompting, reasoning, RAG
- Logarithmic scale = each step is 10× bigger
- MoE models activate only parts of the network
