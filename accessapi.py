import os
import openai
from dotenv import load_dotenv

load_dotenv()

prompt = 'Give me an outline for a course on how to make web applications using bubble'
messages = [{"role": "user", "content": prompt}]

openai_secret_key = os.getenv('OPENAI_SECRET_KEY')

openai.api_key = openai_secret_key

output = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    max_tokens=400,
    temperature=0
)

output_text = output.choices[0].message['content']

print(output_text)
