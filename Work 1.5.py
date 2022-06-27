def count_find_num(primesL, limit):
    k:int = 0
    count = 0
    mx = 0 
    for i in range(1,limit+1):
        number = i
        for j in range(len(primesL)):
            if number % primesL[j] != 0:
                break
            elif number % primesL[j] == 0:
                while(number % primesL[j] == 0):
                    number = number // primesL[j]
                    if number == 1 and primesL[j] == primesL[len(primesL)-1]:
                        count = count +1
                        mx=i
    if count == 0:
        result = []
    else:
        result = [count,mx]
    return result
