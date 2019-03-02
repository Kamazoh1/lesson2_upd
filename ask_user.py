dialogue_dict = {"Как дела?": "Хорошо",
                "Что делаешь?": "Программирую"}

def ask_user(response):
    answer = dialogue_dict.get(response)
    print(answer)
    return answer

while True:
    try:
        response = input('Как дела? ')
        if response == "Хорошо":
            break
        else:
            ask_user(response)
    except KeyboardInterrupt:
        print("\nПока")
        break
