def count_find_num(primesL, limit):
    count = 0
    mx = 0
    mm = 1
    a = 1
    lis = []
    for h in primesL:
        mm *= h
    lis.insert(0,mm)
    mx = mm
    while True:
        point = True
        for j in primesL:
            for k in lis:
                if k * j < limit + 1 and k*j not in lis:
                    a += 1
                    lis.insert(a,k*j)
                    if mx < k*j:
                        mx = k*j
                    point = False
        if point:
            break
    if mx > limit:
        result = []
    else:
        result = [a,mx]
    print(lis)
    return result
