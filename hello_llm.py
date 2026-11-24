import os
import sys
from dotenv import load_dotenv
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": "Explain what an LLM is in 2 sentences."}
    ],
)

print(response.choices[0].message.content)