def insertBT(head, data):
    if head == None:
         head = Node()
         head.val = data
         return head
    if head.val < data:
        head.right = insertBT(head.right, data)
    else:
        head.left = insertBT(head.left, data)
    return head
