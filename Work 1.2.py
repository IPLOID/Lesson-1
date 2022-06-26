def int32_to_ip(int32):
    a = '0'
    b = '0'
    c = '0'
    d = '0'
    y = bin(int32)
    x = y.replace('0b','')
    length = len(x)
    if length <= 8:
        d = str(int(x,2))
    if 8 < length <= 16:
        d = str(int(x[length-8:length:1],2))
        c = str(int(x[0:length-8:1],2))
    if 16 < length <= 24:
        d = str(int(x[length-8:length:1],2))
        c = str(int(x[length-16:length-8:1],2))
        b = str(int(x[0:length-16:1],2))
    if 24 < length <= 32:
        d = str(int(x[length-8:length:1],2))
        c = str(int(x[length-16:length-8:1],2))
        b = str(int(x[length-24:length-16:1],2))
        a = str(int(x[0:length-24:1],2))
    z = a + '.' + b + '.' + c + '.' + d   
    if length > 32:
        z = "Нельзя перевести число в IPv4-адрес"    
    return z
