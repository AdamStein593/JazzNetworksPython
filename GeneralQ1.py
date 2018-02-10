def even_fib():
    fib0 = 1
    fib1 = 1
    index = 0
    sum = 0
    while (index < 100):
        next_val = fib0 + fib1
        fib0 = fib1
        fib1 = next_val
        if (next_val % 2 == 0):
            index +=1
            sum += next_val
    return sum

print(even_fib())
