
def binarysearch(a, n):
    pivot = int(len(a)/2)

    print(a)
    print(pivot)

    if(a[pivot] == n):
        return pivot
    elif(a[pivot] > n):
        return binarysearch(a[:pivot], n)
    else:
        return binarysearch(a[pivot:], n)

def reverse(a):
    for i in range(len(a), 0):
        print(a)

# List implemenation of binary heap
# reverse sorted list fufils the heap condition
def _binarysearch(a, n):
    heap = list.reverse(a); i = 0
    print(heap)

    while(i < len(heap)):
        leftchild = (i*2)+1
        rightchild = (i*2)+2
        pivot = int(len(a)/2)

        if(heap[pivot] == n):
            return heap[pivot]
        elif(heap[leftchild] > heap[pivot]):
            i = leftchild
        elif(heap[rightchild] < heap[pivot]):
            i = rightchild

    return None

a = [1, 4, 7, 8, 12, 31, 100]
reverse(a)

