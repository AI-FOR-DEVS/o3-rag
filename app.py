from openai import OpenAI
from rag_example import search_in_vectorstore

client = OpenAI()

def chat(query, chat_history):
    # Add system message if chat history is empty
    if not chat_history:
        system_message = {
            "role": "system",
            "content": """
                You are a knowledgeable assistant specializing in e-bike rentals in Berlin. Your role is to:
                1. Provide accurate information about e-bike rental services, locations, prices, and regulations in Berlin
                2. Use the provided context to answer questions precisely and factually
                3. If the context doesn't contain relevant information for a question, clearly state that you don't have specific information about that aspect
                4. Maintain a friendly, helpful tone while staying focused on Berlin e-bike rental topics
                5. Never make assumptions or provide information that isn't supported by the context

                When responding:
                - Be concise and direct
                - Include specific details from the context when available
                - Clearly distinguish between information from the context and general knowledge
                - If unsure, ask for clarification rather than making assumptions
            """
        }
        chat_history.append(system_message)

    context = search_in_vectorstore(query)
    prompt_with_context = f"Context: {context}\n\nUser input: {query}"

    chat_history.append({"role": "user", "content": prompt_with_context})

    response = client.chat.completions.create(
        model="o3-mini",
        messages=chat_history,
        stream=True
    )

    complete_response = ""
    
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            complete_response += chunk.choices[0].delta.content
            yield chunk.choices[0].delta.content

    chat_history.append({"role": "assistant", "content": complete_response})