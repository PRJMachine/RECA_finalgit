import openai

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"
openai.api_key = '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'

def calling_cookpt(rolemsg, assistantmsg, usermsg):
    
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