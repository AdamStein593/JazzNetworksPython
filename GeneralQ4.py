def base_convertor(base, value):
    max_base = 0
    power = 0
    while(max_base <= value):
        power += 1
        max_base = pow(base, power)
    power -= 1
    while(power >= 0):
        digit_value = pow(base, power)
        digit = value // digit_value
        value -= digit * digit_value
        power -= 1
        if(digit > 9):
            digit = chr(97 + digit - 10)
        print(digit, digit_value)


base_convertor(16, 1050)