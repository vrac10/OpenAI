
import os
import openai
# model to be used text-davinci-003 openai.api_key = "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"
def generation(text):
    openai.api_key = "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"
    # text = input("Whats your query? : ")
    completion = openai.Completion.create(engine= 'text-davinci-003',prompt = text, max_tokens=1024, n=1, stop=None, temperature=0.5,)
    response = completion.choices[0].text
    return response