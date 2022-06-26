def zeros(n):
    k:int = 0
    i:int = 5      
    while (n/i>=1):
            k = k + n//i
            i = i * 5
    return int(k)
