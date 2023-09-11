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

