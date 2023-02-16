import os
import openai
import time

# openai.api_key = "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"  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
openai.api_key = "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" 

data = open("ChatGPT_API/input.txt",encoding="utf8").read().splitlines()  # read input file

prompt = """Phân loại cảm xúc cho câu sau, theo 3 nhãn: [NEGATIVE],[POSITIVE] và [NEUTRAL]:"""

for item in data:
    prompt += f"\n- {item}"

print(f"Final promt is: \n" + prompt)


def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:", " AI:"]
    )

    return response.choices[0].text


a = time.time()
ans = openai_create(prompt)
b = time.time()
print(f"Request time: {b - a}")  # print request time
print()
print(prompt + ans)
