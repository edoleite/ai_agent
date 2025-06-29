import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
print(f"API key is: {api_key}")  # For debugging

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(model="gemini-2.0-flash-001", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

print(response.text)

x = response.usage_metadata.prompt_token_count
y = response.usage_metadata.candidates_token_count

print(f"Prompt tokens: {x}\nResponse tokens: {y}")