def mergeSorted(A, B):
    if A == None:
        return B
    if B == None:
        return A
    if A.val < B.val:
        A.next = mergeSorted(A.next, B)
        return A
    else:
        B.next = mergeSorted(A, B.next)
        return B