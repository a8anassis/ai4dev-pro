from dotenv import load_dotenv
load_dotenv()
import litellm

message = {"role": "user", "content": "Ποια είναι η πρωτεύουσα της Κρήτης;"}
response = litellm.completion(
    model="anthropic/claude-haiku-5-5",
    messages=[message]
)
print(response.choices[0].message.content)