import os
from openai import OpenAI
from rag import retrieve
from tools import get_order_status
from memory import get_memory, update_memory

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def agent(user_id, message):
    memory = get_memory(user_id)
    context = retrieve(message)

    if "order" in message:
        order_id = "".join(filter(str.isdigit, message))
        tool_result = get_order_status(order_id)
    else:
        tool_result = ""

    prompt = f"""
    You are an AI support agent.
    Context: {context}
    Memory: {memory}
    Tool Output: {tool_result}
    User: {message}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content
    update_memory(user_id, message, reply)
    return reply
