import gradio as gr
from groq import Groq
import json

# --- CONFIG ---
client = Groq(api_key=key)

MODEL = "llama-3.3-70b-versatile"   # Recommended

# --- TOOL FUNCTION ---
def get_train_fare(destination_city: str):
    print(f"\n[SYSTEM] 🚂 Tool Triggered! Searching fare for: {destination_city}")

    prices = {
        "mumbai": "1,600",
        "jaipur": "650",
        "bengaluru": "2,400",
        "kolkata": "1,750",
        "varanasi": "980",
        "chennai": "2,100",
        "agra": "450",
        "amritsar": "800"
    }

    city = destination_city.lower().strip()
    price = prices.get(city)

    if price:
        return {"price": price, "currency": "INR", "status": "available"}
    else:
        return {"error": f"Fare not found for {city}", "status": "unknown"}


# --- TOOL SCHEMA (OpenAI Compatible Format) ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_train_fare",
            "description": "Get train fare from New Delhi to a destination city",
            "parameters": {
                "type": "object",
                "properties": {
                    "destination_city": {
                        "type": "string",
                        "description": "Name of the destination city"
                    }
                },
                "required": ["destination_city"]
            }
        }
    }
]


# --- CHAT FUNCTION ---
def chat(message, history):

    messages = [
        {
            "role": "system",
            "content": """
            You are RailSathi, a helpful Indian Railways assistant.
            When a user asks for ticket price or fare,
            you MUST call the get_train_fare tool.
            After getting the tool result,
            respond politely in natural language.
            Prices are always in INR.
            """
        }
    ]

    # Add history
    for msg in history:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    # Add new user message
    messages.append({"role": "user", "content": message})

    # First API call
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # If tool is called
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]
        arguments = json.loads(tool_call.function.arguments)

        # Execute tool
        result = get_train_fare(**arguments)

        # Add tool call + result to conversation
        messages.append(msg)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })

        # Second API call (Final Answer)
        second_response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        return second_response.choices[0].message.content

    # If no tool needed
    return msg.content


# --- LAUNCH ---
if __name__ == "__main__":
    gr.ChatInterface(
        fn=chat,
        title="🚆 RailSathi AI (Groq Powered)",
        description="Ask for train fares from New Delhi (e.g., 'Price for Mumbai?').",
    ).launch()
