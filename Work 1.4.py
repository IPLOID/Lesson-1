def bananas(s) -> set:
    result = set()
    count = 0
    length = len(s)
    if length == 6 and s == 'banana':
        result.add(s)    
    if length > 6:
        for i in range(length-5) :
                for j in range(i+1,length-4):
                    for k in range(j+1,length-3):
                        for l in range(k+1,length-2):
                            for m in range(l+1,length-1):
                                for n in range(m+1,length):
                                    if s[i]+s[j]+s[k]+s[l]+s[m]+s[n] == 'banana':
                                        hw = s
                                        for zz in range(length):
                                            for z in [i,j,k,l,m,n]:
                                                if zz == z:
                                                    break
                                                elif zz != z and (z > zz or n <zz):
                                                    hw = hw[:zz] + "-" + hw[zz+1:]
                                                    break           
                                        result.add(hw)    
                                        count = count + 1                                                            
    return result
