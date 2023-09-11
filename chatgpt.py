import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content


userPrompt = "What does it mean to be an optimist?"

response = BasicGeneration(userPrompt)

print(response)

