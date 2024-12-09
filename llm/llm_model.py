import os
import requests

# Load the Groq model using the API key from environment variables
def load_groq_model():
    # We don't need to load the model explicitly; we will use the API endpoint to query it.
    # This function just returns the Groq API URL or other necessary information.
    groq_api_url = os.getenv('GROQ_API_URL', 'https://api.groq.com')  # Replace with actual Groq API URL
    return groq_api_url

# Generate an answer using the Groq model
def generate_answer_with_groq(query, retrieved_chunks, model_url):
    context = " ".join(retrieved_chunks)
    prompt = f"Answer the following question: {query}\nContext: {context}"

    # Prepare the API request to the Groq endpoint
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json",
    }

    payload = {
        "query": prompt,
    }

    # Send a POST request to the Groq API (assuming it supports this kind of interaction)
    response = requests.post(f"{model_url}/v1/query", json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get('answer', 'No answer returned')  # Adjust based on API response format
    else:
        return f"Error: {response.status_code}, {response.text}"

