def domain_name(url):
    length = len(url)
    for i in range(length) :
        if url[i] == ':' :
            s = url[i+3:length:1]
        if url[i:i+4:1] == "www.":
            s = url[i+4:length:1]        
    length = len(s)
    for i in range(length-1) :
        if s[i] == '.' :
            su = s[0:i:1]      
    return su
