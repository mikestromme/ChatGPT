import openai
import os
from dotenv import load_dotenv

<<<<<<< HEAD
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()    
=======
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

>>>>>>> 30facc6e005a4121677df2e1fcf4e8f5444a3e3a

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

