# 📘 Study Notes: System Prompts, One-Shot Prompting & the First Step Toward RAG

---

## 🔹 1. Improving the System Prompt

### 🔸 What Is a System Prompt?

The **system prompt**:

- Sets the role of the model
- Defines tone and behavior
- Injects business rules
- Shapes how the assistant responds

📌 It controls the assistant before the user even speaks.

---

### 🔸 Example System Prompt (Clothing Store)

The assistant is told:

- You are a **helpful assistant in a clothes store**
- Encourage customers to buy **items on sale**
- Hats are **60% off**
- Most other items are **50% or 60% off**
- Encourage hats when unsure

This prompt includes:

| Component        | Purpose               |
| ---------------- | --------------------- |
| Context          | Clothes store         |
| Business Rules   | Hats 60% off          |
| Tone             | Gentle encouragement  |
| Strategy         | Upsell hats           |
| Example Response | Demonstrates behavior |

---

## 🎯 2. One-Shot Prompting

### 🔸 What Is One-Shot Prompting?

**One-shot prompting**:

- Provide **one example**
- Model learns the pattern
- Replicates similar structure

Example:

> If customer says: “I want a hat”
> Reply with: “Wonderful! We have hats on sale…”

📌 The example teaches the model the desired format.

---

## 🔄 3. Multi-Shot Prompting

### 🔸 What Is Multi-Shot Prompting?

When you provide:

- Multiple example scenarios
- Multiple example responses

Example addition:

> If customer asks for shoes →
> Say shoes are not on sale → Suggest hats

Now the model has:

- Multiple behavioral examples
- More structured guidance

📌 More examples = clearer behavior control.

---

## 🧠 4. Dynamic System Prompts (Context Injection)

### 🔸 What Was Demonstrated?

System prompt changes dynamically based on user input:

```python
if "belt" in user_message:
    system_prompt += "The store does not sell belts..."
```

---

### 🔸 What Happens?

If user asks:

> “I want a belt”

Then the system prompt:

- Gets extra information
- Tells the model:
  - Store doesn’t sell belts
  - Suggest other items

📌 The model behaves differently because the **prompt changed**.

---

## 📦 8. Why Not Just Add Everything to the Prompt?

You _could_ always include:

- All products
- All rules
- All pricing
- All store policies

But problems:

- Context window grows too large
- Token costs increase
- Accuracy degrades
- Noise increases

📌 Selective context injection is smarter.

---

## 🧠 9. This Is Inference-Time Scaling

Important distinction:

| Training-Time Scaling | Inference-Time Scaling |
| --------------------- | ---------------------- |
| Bigger model          | Better prompting       |
| More parameters       | More relevant context  |
| Expensive             | Efficient              |

This lab demonstrates:

- **Inference-time scaling**
- Same model
- Smarter prompt usage

---

## 🏢 10. Business Applications

This technique enables:

### 🔹 Conversational Agents

- Customer support bots
- Sales assistants
- Product recommendation bots

---

### 🔹 Adding Business Value

Instead of:

> “Just use ChatGPT”

You:

- Inject proprietary business knowledge
- Control tone
- Control behavior
- Insert company rules

📌 That’s where companies add value.

---

## 🚀 11. Key Engineering Insight

LLMs are:

- Powerful out of the box

But become:

- Business-grade tools
- When you add context + rules

Prompt = Knowledge + Control + Strategy

---

# ⚡ Quick Revision

- **System prompt** defines behavior
- **One-shot prompting** = one example
- **Multi-shot prompting** = multiple examples
- Dynamic prompt updates = context injection
- This is the foundation of **RAG**
- RAG = retrieve → insert → generate
- Better context = better outputs
- Business value comes from domain-specific context

---

# 1️⃣ RAG (Retrieval-Augmented Generation)

---

## 🔹 Simple Definition

RAG = LLM + Your External Data

It allows a language model to **search documents first**, then generate an answer using that retrieved information.

---

## 🔹 Why RAG is Needed

Problem with normal LLM:

- It only knows what it was trained on.
- It can hallucinate.
- It doesn't know your private data (PDFs, company DB, etc.).

RAG solves this by:

- Fetching relevant documents
- Feeding them into the model
- Generating accurate answers

---

## 🔹 Architecture Diagram (Explained in Words)

Imagine this pipeline:

User Question
↓
Convert question into vector
↓
Search vector database
↓
Retrieve relevant documents
↓
Send documents + question to LLM
↓
Generate final answer

That is RAG.

---

## 🔹 Components Involved

1. **Documents** – PDFs, DB data, websites
2. **Embedding Model** – Converts text into vectors
3. **Vector Database** – Stores embeddings (e.g., FAISS, Pinecone)
4. **Retriever** – Finds similar documents
5. **LLM** – Generates final answer
6. **Prompt Template** – Controls how answer is generated

---

## 🔹 Data Flow Step-by-Step

1. You upload documents.
2. Documents are split into chunks.
3. Each chunk is converted into embeddings.
4. Stored inside a vector database.
5. User asks a question.
6. Question is converted into embedding.
7. Vector DB finds similar chunks.
8. Those chunks are sent to LLM.
9. LLM generates answer based only on retrieved data.

---

## 🔹 Python Pseudo Code

```python
# Step 1: Load documents
docs = load_documents("company_data.pdf")

# Step 2: Split documents
chunks = split_into_chunks(docs)

# Step 3: Create embeddings
embeddings = embed_model.embed(chunks)

# Step 4: Store in vector DB
vector_db.store(chunks, embeddings)

# Step 5: User question
question = "What is refund policy?"

# Step 6: Retrieve relevant chunks
relevant_docs = vector_db.search(question)

# Step 7: Send to LLM
response = llm.generate(
    prompt=f"Answer using this context: {relevant_docs}\nQuestion: {question}"
)

print(response)
```

---

## 🔹 When to Use RAG

✅ Chatbot using company data
✅ Legal document Q&A
✅ Medical research assistant
✅ Internal enterprise knowledge base
✅ AI tutor with textbooks

---

## 🔹 When NOT to Use RAG

❌ Simple chatbot with no external data
❌ Small static FAQs
❌ When latency must be extremely low

---

## 🔹 Common Interview Questions

1. What problem does RAG solve?
2. Difference between fine-tuning and RAG?
3. What is embedding?
4. What is vector similarity search?
5. How do you reduce hallucination in RAG?
6. What is chunking strategy?
7. What is context window limitation?

---

# 2️⃣ LangChain

---

## 🔹 Simple Definition

LangChain is a framework to build applications using LLMs.

It helps you connect:

- LLMs
- Tools
- Memory
- Vector databases
- Agents

---

## 🔹 Why LangChain is Needed

LLM alone = just text generation.

Real apps need:

- Retrieval
- Memory
- Tool calling
- Multi-step reasoning

LangChain organizes this.

---

## 🔹 Architecture Diagram (In Words)

User
↓
Prompt Template
↓
Chain
↓
LLM
↓
Output

OR (Advanced)

User
↓
Agent
↓
Tool Selection
↓
Call Tool
↓
Return Result
↓
LLM Final Response

---

## 🔹 Components

1. **LLM Wrapper**
2. **PromptTemplate**
3. **Chains**
4. **Memory**
5. **Agents**
6. **Tools**
7. **Vector Stores**

---

## 🔹 Data Flow Step-by-Step (Simple Chain)

1. User sends input.
2. Prompt template formats it.
3. Chain sends it to LLM.
4. LLM generates response.
5. Output returned.

---

## 🔹 Python Pseudo Code

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI()

template = "Explain {topic} in simple terms."
prompt = PromptTemplate(template=template)

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run(topic="RAG")

print(response)
```

---

## 🔹 When to Use LangChain

✅ Building RAG systems
✅ Tool-calling chatbots
✅ Multi-step workflows
✅ AI agents
✅ Chatbots with memory

---

## 🔹 When NOT to Use LangChain

❌ Simple API call to GPT
❌ Very small experimental scripts
❌ When you need ultra-lightweight system

---

## 🔹 Common Interview Questions

1. What is a Chain?
2. Difference between Agent and Chain?
3. What is Memory?
4. What is Tool calling?
5. What is Runnable?
6. How does LangChain support RAG?

---

# 3️⃣ Agentic AI

---

## 🔹 Simple Definition

Agentic AI = AI that can think, decide, and take actions autonomously.

Instead of just answering,
it can:

- Plan
- Use tools
- Make decisions
- Execute steps

---

## 🔹 Why Agentic AI is Needed

Normal LLM:
User → Answer

Agentic AI:
User → Plan → Tool → Analyze → Decide → Repeat → Final answer

Used for automation and complex workflows.

---

## 🔹 Architecture Diagram (In Words)

User Goal
↓
Planner (LLM)
↓
Select Tool
↓
Execute Tool
↓
Observe Result
↓
Decide Next Step
↓
Repeat until goal achieved
↓
Final Output

This is called a **Reason-Act-Observe loop**.

---

## 🔹 Components

1. LLM (Reasoning brain)
2. Tools (APIs, DB, Calculator)
3. Memory
4. Planner
5. Execution Engine

---

## 🔹 Data Flow Step-by-Step

Example: “Book cheapest flight tomorrow”

1. Agent understands goal.
2. Decides to call flight search API.
3. Gets flight data.
4. Compares prices.
5. Chooses cheapest.
6. Calls booking API.
7. Confirms booking.

Multiple thinking steps.

---

## 🔹 Python Pseudo Code

```python
while not task_completed:

    plan = llm.generate("What should I do next?")

    if "search flight" in plan:
        result = search_flight_api()

    elif "compare prices" in plan:
        result = compare_prices()

    elif "book flight" in plan:
        result = book_ticket()
        task_completed = True

print("Task Completed")
```

---

## 🔹 When to Use Agentic AI

✅ Workflow automation
✅ Autonomous research assistant
✅ Trading bots
✅ AI copilots
✅ Complex multi-step decision systems

---

## 🔹 When NOT to Use

❌ Simple FAQ chatbot
❌ Single-step question answering
❌ Low latency critical systems

---

## 🔹 Common Interview Questions

1. What is an AI Agent?
2. What is ReAct pattern?
3. Difference between RAG and Agent?
4. What is tool calling?
5. What is memory in agents?
6. Risks of autonomous AI systems?

---

# 🔥 Final Comparison

| Feature              | RAG                    | LangChain      | Agentic AI                 |
| -------------------- | ---------------------- | -------------- | -------------------------- |
| Purpose              | Add external knowledge | Build LLM apps | Autonomous decision-making |
| Uses Vector DB       | Yes                    | Optional       | Optional                   |
| Uses Tools           | No (basic RAG)         | Yes            | Yes                        |
| Multi-step reasoning | No                     | Limited        | Yes                        |
| Autonomous           | No                     | Sometimes      | Yes                        |

---

# 🧠 Real-World Perspective

- RAG = Knowledge
- LangChain = Framework
- Agentic AI = Autonomy

---
