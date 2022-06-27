def count_find_num(primesL, limit):
    count = 0
    mx = 0
    mm = 1
    a = 0
    lis = []
    length = len(primesL)
    for h in range(length):
        mm = mm * primesL[h]
    for i in range(mm,limit+1,mm):
        number = i
        for j in range(len(primesL)):
            if (number % primesL[j] == 0):
                while(number % primesL[j] == 0):
                    number = number // primesL[j]
            if number == 1:
                count = count +1
                mx=(i)
                break      
    if count == 0:
        result = []
    else:
        result = [count,mx]
    return result
