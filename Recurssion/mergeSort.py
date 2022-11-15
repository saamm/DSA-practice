def mergesort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        larray = nlist[:mid]
        rarray = nlist[mid:]
        mergesort(larray)
        mergesort(rarray)
        
        i,j,k = 0, 0, 0
        while i < len(larray) and j < len(rarray):
            if larray[i] <= rarray[j]:
                nlist[k] = larray[i]
                i += 1
            else:
                nlist[k] = rarray[j]
                j += 1
            k += 1
        while i < len(larray):
            nlist[k] = larray[i]
            i += 1
            k += 1
        while j < len(rarray):
            nlist[k] = rarray[j]
            j += 1
            k += 1
            
num = [5,2,6,8,3]
print(mergesort(num))
print(num)
            
            
                
    