def get_multiplied_digits(number):

    str_number = str(number)

    first = int(str_number[0])

    # Если первая цифра равна 0, пропускаем её
    if first == 0:
        if len(str_number) > 1:
            return get_multiplied_digits(int(str_number[1:]))
        else:
            return 1 # Если осталась только 0
        
    # Если длина строки больше 1, продолжаем рекурсию    
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    
    return first
    
result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)