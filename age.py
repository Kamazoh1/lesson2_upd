def age_2_place(age):
    place = 'Сколько можно у родителей на шее сидеть? Иди работай!'
    if age < 0:
        place = "Рано тебе еще искать свое место в жизни!"
    elif age < 3:
        place = "Наслаждайся бездельем дома"
    elif age < 7:
        place = 'Тебе пора в детский сад!'
    elif age < 17:
        place = 'Вперед за знаниями, юный падаван!'
    elif age < 22:
        place = 'Чудесные годы студенчества... Но сессия уже близко!'
    return place


age = input('Введите ваш возраст: ')
if age.isdigit():
    age = int(age)
else:
    raise TypeError("У нормальных людей в возрасте только цифры")


actual_place = age_2_place(age)

print(actual_place)

