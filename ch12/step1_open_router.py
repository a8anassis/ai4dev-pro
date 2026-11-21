import os

from dotenv import load_dotenv
load_dotenv()
import litellm

MODEL = os.getenv("MODEL_OPENROUTER_FREE")

message = {"role": "user", "content": "Ποια είναι η πρωτεύουσα της Κρήτης;"}
response = litellm.completion(
    model= MODEL,
    messages=[message]
)

print(response.choices[0].message.content)