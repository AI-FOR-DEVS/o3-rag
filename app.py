from openai import OpenAI
from rag_example import search_in_vectorstore

client = OpenAI()

def chat(query):
    context = search_in_vectorstore(query)
    prompt_with_context = f"Context: {context}\n\nUser input: {query}"

    response = client.chat.completions.create(
        model="o3-mini-2025-01-31",
        messages=[{"role": "user", "content": prompt_with_context}],
        stream=True
    )
    
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

for chunk in chat("Where is the nearest bike station? I'm near Berlin Ostbahnhof. Please list all locations that are close by."):
    print(chunk, end='', flush=True)