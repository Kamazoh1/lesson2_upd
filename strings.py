def strings_processing(string1, string2):
    if type(string1) == str and type(string2) == str:
        if string1 == string2:
            return 1
        if len(string1) > len (string2):
            return 2
        if string2 == 'learn':
            return 3
    else:
        return 0


string1 = str(input("Input string1: "))
string2 = str(input("Input string2: "))

string_check = strings_processing(string1, string2)

print(string_check)


