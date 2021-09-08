    
def binarysearch(a, n):
    pivot = int(len(a)/2)

    if(len(a) < 1):
        return None
    elif(a[pivot] == n):
        return pivot
    elif(a[pivot] > n):
        return binarysearch(a[:pivot], n)
    else:
        s = binarysearch(a[pivot+1:], n)
        return (s + pivot + 1) if s != None else None

a = [1, 4, 7, 8, 12, 31]

i = 7
print(a)
print(f'{i} in index: {binarysearch(a, i)}')

