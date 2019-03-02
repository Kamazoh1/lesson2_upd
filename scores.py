
school_marks = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '4b', 'scores': [4,4,5,2,2]},
                {'school_class': '4c', 'scores': [2,1,4,3,2]},
                {'school_class': '5a', 'scores': [3,4,5,4,2]}]


# i = school_marks['scores']
summ = 0
count = 0
summ_school = 0
for score in school_marks:
#      print(score['school_class'])
    for marks in score['scores']:
        #  print(len(score['scores']))
         summ += marks
    avg_mark = summ / len(score['scores'])
    print('Средний балл по классу', score['school_class'],avg_mark)
    summ_school += summ
    summ = 0
    count += len(score['scores'])
avg_mark = summ_school / count
# print(summ)
# print(count)
print('Средний балл по школе',avg_mark)
# print(*school_marks[0]['scores'])
