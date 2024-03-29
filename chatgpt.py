import openai
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    userPrompt = "In T-sql how do I select all records from a table?"

    response = BasicGeneration(userPrompt)

    print(response)


def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content


if __name__ == '__main__':
    main()

    

