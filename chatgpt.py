import openai


openai.api_key = "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"

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

