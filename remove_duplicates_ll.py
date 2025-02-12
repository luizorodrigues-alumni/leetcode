# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy_node = ListNode(val=-200, next=head)
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        
        else:
            head = head.next        
    
    return dummy_node.next

head = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=None)))
deleteDuplicates(head)
print(head.val)
print(head.next.next)



# Without dummy node (also works)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
            
#             else:
#                 current = current.next        
    
#         return head