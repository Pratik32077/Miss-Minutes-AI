import openai
from config import apikey

openai.api_key = apikey

completion = openai.Completion.create(
    engine="text-davinci-003",  # or "text-davinci-003" for the previous version
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60
)

print(completion.choices[0].text.strip())
