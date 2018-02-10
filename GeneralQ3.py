def merge_sort(lst_a, lst_b):
    merged = []
    while len(lst_a)!= 0 or len(lst_b)!= 0 :
        if (len(lst_a)== 0):
            merged = merged + lst_b
            lst_b = []
        elif (len(lst_b)== 0):
            merged = merged + lst_a
            lst_a = []
        elif(lst_a[0] > lst_b[0]):
            merged.append(lst_b[0])
            lst_b.pop(0)
        else:
            merged.append(lst_a[0])
            lst_a.pop(0)
    return merged

b = [1,3,5,9,10]
a = [2,4,6, 7, 8, 10, 11, 12]
print(merge_sort(a, b))
