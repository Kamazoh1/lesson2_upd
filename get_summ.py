def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)

        summ = num_one + num_two
        return summ
    except ValueError:
        print("Не могу опознать число. Проверь входные данные.")


num_one = 2
num_two = 's'
get_summ(num_one, num_two)