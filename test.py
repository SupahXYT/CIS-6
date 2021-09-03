#!/usr/bin/env python3

def merge(left, right): # Returns merged list (sorted)
    left = left[0]

    if(len(right) < 1):
        right = []
    else:
        right = right[0]
    merge = []

    while(len(left) > 0 or len(right) > 0): # While there exists elements in either list
        while(len(left) > 0):
            if(len(right) > 0 and left[0] < right[0]):
                merge.append(left.pop(0))
            elif(not(len(right) > 0)):
                merge.append(left.pop(0))
            else:
                merge.append(right.pop(0))
        while(len(right) > 0):
            if(len(left) > 0 and right[0] < left[0]):
                merge.append(right.pop(0))
            elif(not(len(left) < 0)):
                merge.append(right.pop(0))
            else:
                merge.append(left.pop(0))

    return merge


a = [[7], [6], [2], [5], [1], [3], [7]]

pairs = int(len(a)/2) + len(a)%2

print(a)

# Begin mergesort
#while(len(a) > 1):
def mergesort(a):
    r = []

    i = 0
    while(i < len(a)):

        left = a[i:i+1]
        right = a[i+1:i+2]

        r.append(merge(left, right))
        i += 2
    
    return r

while(len(a) > 1):
    a = mergesort(a)

print(a[0])
# print(mergesort(a))
# mergesort([[6, 7], [2, 5], [1, 3], [7]])
# mergesort([[2, 5, 6, 7], [1, 3, 7]])
# mergesort([[[6], [7]], [[2], [5]], [[1], [3]], [[7]]])