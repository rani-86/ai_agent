from openai import OpenAI
from rag import retrieve
from tools import get_order_status
from memory import get_memory, update_memory

client = OpenAI()

def agent(user_id, message):
    memory = get_memory(user_id)
    context = retrieve(message)

    # tool detection (basic logic)
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
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response.choices[0].message.content
    update_memory(user_id, message, reply)

    return reply