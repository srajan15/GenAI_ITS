# 📘 Study Notes: Tool Calling in LLMs

---

# 🔧 1. What Are Tools in LLMs?

## 🔹 Definition

A **tool** is:

> An external function or piece of code that the LLM can request your program to execute.

The LLM itself:

- Does NOT execute code
- Does NOT access your database
- Does NOT run Python

It only:

- Generates text (tokens)

But it can generate tokens that **request a tool call**.

---

# 🧠 2. Why Tools Matter

Tools are foundational for:

- **Agentic AI**
- Commercial chatbots
- Real-world automation
- Workflow systems

Tools allow an LLM to:

- Retrieve database data
- Perform calculations
- Book tickets
- Execute Python
- Call APIs
- Run test cases

📌 Without tools, LLMs are just smart text generators.
With tools, they become interactive systems.

---

# 🤔 3. The Big Confusion: How Can a Neural Network Run Code?

This is where many people get confused.

You might think:

> "How can a neural network suddenly run Python code on my computer?"

Important:

### ❌ The LLM does NOT execute your code.

It simply generates tokens like:

```
Please call tool: fetch_ticket_price(city="Paris")
```

That's it.

---

# ⚙️ 4. What Actually Happens (Real Flow)

Here is the **real tool-calling flow**:

---

## Step 1: You Send First Message to LLM

You tell it:

- Your task
- Available tools
- How to request tool usage

Example:

> "If you need ticket prices, reply with:
> use_tool: fetch_ticket_price(city_name)"

---

## Step 2: LLM Responds

Instead of answering directly, it replies:

```
use_tool: fetch_ticket_price(city="Paris")
```

It is just generating tokens.

Nothing magical.

---

## Step 3: Your Code Checks Response

Your Python code says:

```python
if "use_tool" in response:
    call_the_function()
```

Your code runs the tool.

NOT the LLM.

---

## Step 4: You Call LLM Again

Now you send a second request:

Conversation history:

- User question
- LLM tool request
- Tool result

And say:

> "Here is the tool result. Now answer the question."

---

## Step 5: LLM Generates Final Answer

It now produces:

> "The flight to Paris costs $450."

Still just generating tokens.

---

# 📦 5. Why This Works

Because in the **first prompt**, you told the LLM:

- Tools exist
- How to call them
- What format to use (usually JSON)

LLMs are trained on structured formats like JSON.

So they know how to generate:

```json
{
  "tool_call": "fetch_ticket_price",
  "arguments": { "city": "Paris" }
}
```

That’s all tool calling is.

---

# 🧪 6. Simple Demonstration Example

Prompt given to ChatGPT:

> You are an airline support agent.
> If you need ticket prices, respond with:
> "use tool to fetch ticket price for CITY"

User asks:

> "How much is a flight to Paris?"

ChatGPT replies:

> "Use tool to fetch ticket price for Paris"

That’s tool calling.

Nothing magical.

Just structured token generation.

---

# 🧩 7. Key Concept: LLMs Are Stateless

Every call to an LLM:

- Does not remember past calls
- Only sees what you send in the prompt

So tool calling works by:

- Including conversation history
- Including tool responses
- Letting LLM respond based on updated context

📌 Tool calls are just conversation messages.

---

# 🤖 8. Tools = Building Blocks of Agentic AI

Agentic AI requires:

- LLM
- Tools
- Loop

Tool calling enables:

- Database lookups
- Booking systems
- Code execution
- API calls
- Multi-step workflows

Without tools → no real autonomy.

---

# 🏢 9. Business Applications of Tools

Tools enable:

### 🔹 Airline booking bots

### 🔹 Customer support systems

### 🔹 Database-powered assistants

### 🔹 Financial calculators

### 🔹 Inventory systems

### 🔹 Code interpreters

Tools transform:

> LLM from text generator
> → into action-capable assistant.

---

# ⚠️ 10. Important Takeaway

LLMs:

- Do NOT run your code
- Do NOT control your system

They only:

- Predict tokens
- Suggest calling tools

Your application:

- Executes the tools
- Sends results back
- Maintains control

This is safe and controlled.

---

# ⚡ Quick Revision

- **Tool = external function**
- LLM never runs code directly
- LLM generates tool request text
- Your program executes the tool
- You call LLM again with tool result
- Tool calling = structured token generation
- Foundation of **Agentic AI**

---

Here are your **perfect structured study notes** for revision 👇

---

# 📘 Study Notes: Typical Uses of Tools in LLM Systems

---

# 🔧 1️⃣ What Are Tools Used For?

Tools allow an LLM to:

- Access external systems
- Perform actions
- Execute logic
- Interact with real-world systems

Remember:

> LLMs generate text.
> Tools allow them to act.

---

# 🗄️ 2️⃣ Common Tool Use Cases

---

## 🔹 1. Database Lookup

### 📌 Use Case:

- Fetch user information
- Retrieve ticket prices
- Check inventory
- Access product details

### Example:

User:

> “How much is a flight to Paris?”

Tool:

```python
fetch_ticket_price("Paris")
```

Why needed:

- LLM training data may be outdated
- Real-time data requires database access

---

## ✈️ 2. Taking Actions

LLMs can request tools that:

- Book meetings
- Reserve tickets
- Place orders
- Update CRM systems
- Send emails

Example Flow:

1. User: “Book me a flight to London.”
2. LLM: “Call booking tool.”
3. Your system books ticket.
4. LLM confirms booking.

📌 This turns LLM into a task-performing assistant.

---

## 🧮 3. Doing Calculations

LLMs are:

- Not reliable at math
- Not deterministic

So we give them:

- A math tool
- A calculator function

Example:

```python
def calculate(expression):
    return eval(expression)
```

ChatGPT likely uses similar internal tools.

📌 Tool ensures precision.

---

## 🧑‍💻 4. Code Execution (Coder Agent)

You can give an LLM a tool that:

- Executes Python
- Runs scripts
- Tests code
- Processes data

Often done in:

- Docker container
- Sandboxed environment

This is called a:

> **Coder Agent**

Important clarification:

A coder agent is not just:

- “An agent that writes code”

It is:

- An agent that can execute code to complete tasks.

Example:

- Analyze CSV
- Run simulation
- Generate chart
- Debug code

---

## 📊 5. UI Interaction

Tools can:

- Generate charts
- Update dashboard
- Modify frontend
- Display graphs instantly

Example:
User:

> “Show me sales trend.”

Tool:

- Generate chart
- Render on screen

📌 This creates interactive AI applications.

---

# 🤖 3️⃣ Tools in Agentic AI (Most Exciting Use)

Tools are the foundation of **Agentic AI**.

Two major patterns:

---

## 🔹 Pattern 1: Tool = Another LLM Call

An LLM can have tools like:

- Tool A → Calls another LLM
- Tool B → Calls specialized LLM
- Tool C → Calls summarization model

So the main LLM becomes an **orchestrator**.

It decides:

- Which sub-model to call
- In what order
- For what task

📌 This enables multi-model workflows.

---

## 🔹 Pattern 2: Tool = Planning & Looping System

You can give LLM:

- A task planner tool
- A to-do list manager
- A progress tracker

Example Flow:

1. LLM creates plan:
   - Step 1
   - Step 2
   - Step 3

2. Executes step-by-step

3. Checks progress

4. Refines plan

5. Continues until done

This creates:

> **Agentic Loop**

LLM in loop + tools = Autonomous agent behavior.

You saw this in:

- Claude Code
- GPT Agent workflows

---

# 🔄 4️⃣ What Is an Agentic Loop?

Definition:

> An LLM repeatedly calls itself with tool access until task completion.

Structure:

```
Input → LLM → Tool → LLM → Tool → LLM → Final Output
```

This enables:

- Autonomy
- Multi-step reasoning
- Task completion

---

# 🧠 5️⃣ Why Tools Are Essential

Without tools:

- LLM = Smart text predictor

With tools:

- LLM = Action-capable AI system

Tools enable:

- Automation
- Real-time data
- Business integration
- Multi-step workflows
- Agent systems

---

# 🏢 6️⃣ Business Applications

Tools power:

- Customer support bots
- Airline booking systems
- Sales assistants
- Financial calculators
- Inventory management
- Code assistants
- Data dashboards
- Autonomous agents

---

# ⚡ Quick Revision

- Tools = external functions
- LLM does NOT execute code
- Your system executes tools
- Tools enable:
  - Database lookup
  - Actions
  - Math
  - Code execution
  - UI updates

- Tools are foundation of Agentic AI
- Two core agent patterns:
  - LLM orchestrates other LLMs
  - LLM in loop with planning tool
