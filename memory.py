# memory.py
memory_store = {}

def get_memory(user_id):
    return memory_store.get(user_id, [])

def update_memory(user_id, message, response):
    if user_id not in memory_store:
        memory_store[user_id] = []
    memory_store[user_id].append({"user": message, "bot": response})