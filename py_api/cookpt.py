import gpt_oracle

# 질문 작성하기
query_ingredients = input("가지고 있는 요리재료 : ")
query_ingredients = str("현재 가지고 있는 요리재료는 " + str(query_ingredients) + "입니다. ")
assistantmsg = ''

while True:
    print("이 재료들을 가지고 가능한 요리를 알고 싶어요[11]")
    print("이 재료들을 가지고 가능한 중화 요리를 알고 싶어요[12]")
    print("이 재료들을 가지고 가능한 프랑스 요리를 알고 싶어요[13]")
    print("이 재료들을 가지고 가능한 이탈리아 요리를 알고 싶어요[14]")
    print("이 재료들을 가지고 가능한 일본 요리를 알고 싶어요[15]")
    print("이 재료들을 가지고 가능한 한국 요리를 알고 싶어요[16]")
    print("이 재료들을 가지고 가능한 동남아 요리를 알고 싶어요[17]")
    print("")
    print("특정 요리를 만들고 싶은데, 지금 가진 재료 외에 더 뭐가 필요한지 궁금해요[31]")
    print("지금 가진 재료와는 상관없이, 제가 원하는 요리의 레시피가 궁금해요[41]")
    print("이 외에, 요리에 대한 질문이 있습니다[51]")
    mode = int(input("요구코드 입력[0=종료] : "))
    if mode//10 == (1 or 2):
        if mode == 11:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 요리를 알고 싶어요.'
        elif mode == 12:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 중화요리를 알고 싶어요.'
        elif mode == 13:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 프랑스 요리를 알고 싶어요.'
        elif mode == 14:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 이탈리아 요리를 알고 싶어요.'
        elif mode == 15:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 일본 요리를 알고 싶어요.'
        elif mode == 16:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 한국 요리를 알고 싶어요.'
        elif mode == 17:
            query_demand = query_ingredients + '이 재료들만을 가지고 만들 수 있는 동남아 요리를 알고 싶어요.'
        else:
            mode = '잘못된 입력'
    elif mode == 31:
        cooking_target = input('무슨 요리를 만들고 싶으세요 : ')
        query_demand = query_ingredients + cooking_target + '를 요리하고 싶은데, 지금 가지고 있는 재료 외에 어떤 요리재료가 더 필요한지, 또는 어떤 요리재료가 있으면 더 맛있을지 알고싶어요.'
    elif mode == 41:
        cooking_target = input('레시피를 알고 싶으신 요리를 알려주세요 : ')
        query_demand = cooking_target + '를 요리하고 싶은데, 맛있게 만드는 방법을 알려주세요.'
    elif mode == 51:
        cooking_target = input('요리사에게 물어보고 싶은 점이 있나요 : ')
        query_demand = cooking_target
    elif mode == 0:
        exit()
    else:
        mode = '잘못된 입력'
    print("답변 준비 중...")
    print(f" [debug] mode : {mode}\n [debug] assistantmsg : {assistantmsg}\n [debug] query : {query_demand}")

    role = int(str(mode)[0])
    if role == 1: #일반 봇
        rolemsg = '당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.'
    elif role == 2: #일반-예비 봇
        rolemsg = '당신은 요리사 입니다. 가지고 있는 재료만 알면 어떤 요리가 가능한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.'
    elif role == 3: #추가재료 봇
        rolemsg = '당신은 요리사 입니다. 원하는 요리를 만들고, 더 맛있게 하기 위해서는 지금 가지고 있는 재료 외에 어떤 요리재료가 더 필요한지 알고 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.'
    elif role == 4: #레시피 봇
        rolemsg = '당신은 요리사 입니다. 요청하는 요리를 만들기 위한 요리 재료와 조리법, 순서를 가르쳐 줄 수 있습니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.'
    elif role == 5: #자유질문 봇
        rolemsg = '당신은 요리사 입니다. 요리나 음식 분야 외의 질문은 거절하며, 요리에 대한 자부심이 강하기 때문에 묻는 말에 반말로, 간결하게 대답합니다.'

    answer = gpt_oracle.oracle(rolemsg, assistantmsg, query_demand)
    assistantmsg = answer
    print('\n', answer, '\n')