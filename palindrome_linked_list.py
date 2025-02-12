# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    og_arr = arr.copy()
    arr.reverse()
    if arr == og_arr:
        return True
    else:
        return False
    

node_1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1, next=None))))


print(isPalindrome(node_1))
