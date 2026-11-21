"""chat με ιστορικό μνήμης + streaming"""
import os

from dotenv import load_dotenv
load_dotenv()
import litellm

MODEL = os.getenv("MODEL")

messages = []    # το ιστορικό της συνομιλίας

while True:
    try:
        user_input = input("Ask ai4dev (ή 'exit' για έξοδο): ")
        if user_input.lower() == 'exit':
            break

        messages.append({"role": "user", "content": user_input})

        response = litellm.completion(
            model= MODEL,
            messages=messages,          # όλο το ιστορικό της συνομιλίας
            stream=True
        )

        print("Model: ", end="")
        parts = []

        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                print(delta, end="", flush=True)
                parts.append(delta)

        print()  # νέα γραμμή μετά την απάντηση

        reply = ''.join(parts)
        messages.append({"role": "assistant", "content": reply})  # προσθήκη

    except litellm.AuthenticationError:
        print("Σφάλμα: Μη έγκυρη ή ληγμένη κλειδί API. Ελέγξτε το αρχείο .env.")
        messages.pop()
    except litellm.RateLimitError:
        print("Σφάλμα: Υπερβολικός αριθμός αιτημάτων. Περιμένετε λίγο πριν ξαναδοκιμάσετε.")
        continue      # messages.pop()
    except litellm.APIConnectionError as e:
        print("Σφάλμα: Πρόβλημα σύνδεσης με το API: {e}.")
        messages.pop()
    except litellm.APIError as e:
        print("Σφάλμα: Σφάλμα από το API: {e}.")
        messages.pop()