def list_sum(integers):
    sum = 0;
    for i in range(len(integers)):
        integer = integers[i]
        if(integer % 2 == 0):
            sum += integer * integer
    return sum;

