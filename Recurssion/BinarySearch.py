def binarySearch(A, l, r, num):
    if l > r:
        return -1
    mid = (l+r)//2
    if A[mid] == num:
        return mid
    if A[mid] > num:
        return binarySearch(A, l, mid, num)
    return binarySearch(A, mid+1 , r ,num)

A = [1,2,3,10]
num = 10
print(binarySearch(A, 0, len(A) - 1, 10))
