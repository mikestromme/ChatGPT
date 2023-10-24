import openai
import os
from dotenv import load_dotenv

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()    

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

    openai.api_key = open_file('key_openai.txt').strip()

    userPrompt = "What does it mean to be an optimist?"

    response = BasicGeneration(userPrompt)

    print(response)

