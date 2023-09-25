import openai

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"
openai.api_key = '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'

def oracle(rolemsg, assistantmsg, usermsg):
    
    # 메시지 설정하기
    messages = [
            {"role": "system", "content": rolemsg},
            {"role": "assistant", "content": assistantmsg},
            {"role": "user", "content": usermsg}
    ]
    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    return response['choices'][0]['message']['content']