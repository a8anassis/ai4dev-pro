import os

from dotenv import load_dotenv
load_dotenv()
import litellm

MODEL = os.getenv("MODEL")

message = {"role": "user", "content": "Ποια είναι η ιστορία της Κρήτης;"}
response = litellm.completion(
    model= MODEL,
    messages=[message],
    stream=True
)

for chunk in response:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)

print()