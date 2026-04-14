import httpx

MEMORY_URL = "http://localhost:8100"
OLLAMA_URL = "http://localhost:11434"

def store_memory(content: str, tags: list = []):
    r = httpx.post(f"{MEMORY_URL}/api/memories",
                   json={"content": content, "tags": tags}, timeout=30)
    return r.json()

def search_memory(query: str, limit: int = 5):
    r = httpx.post(f"{MEMORY_URL}/api/search",
                   json={"query": query, "limit": limit}, timeout=30)
    return r.json()

def chat_with_memory(user_message: str):
    try:
        results = search_memory(user_message)
        memories = results.get("results", [])
        context = "\n".join([m["memory"].get("content", "") for m in memories])
        print(f"[memory] found {len(memories)} results")
    except Exception as e:
        context = ""
        print(f"[memory] search failed: {e}")

    prompt = f"შენ გაქვს ეს მეხსიერება:\n{context}\n\nმომხმარებელი: {user_message}" if context else user_message

    print("[ollama] sending request...")
    with httpx.Client(timeout=600) as client:
        r = client.post(f"{OLLAMA_URL}/api/chat", json={
            "model": "gemma4:26b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        })

    response = r.json()["message"]["content"]
    print(f"[ollama] ✅ {len(response)} chars")

    try:
        store_memory(f"Q: {user_message}\nA: {response}", ["conversation"])
        print("[memory] stored ✅")
    except Exception as e:
        print(f"[memory] store failed: {e}")

    return response

if __name__ == "__main__":
    print(chat_with_memory("Phase 1 რა გავაკეთეთ?"))
