# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Dummy node to simplify list manipulation
    merged_list = ListNode(val=0)  
    current_merged_list = merged_list

    while list1 and list2:
        if list1.val <= list2.val:
            current_merged_list.next = list1
            list1 = list1.next
        else:
            current_merged_list.next = list2
            list2 = list2.next

        current_merged_list = current_merged_list.next

    if list1:
        current_merged_list.next = list1
    elif list2:
        current_merged_list.next = list2

    return merged_list.next

list_1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
list_2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
print(mergeTwoLists(list1=list_1, list2=list_2))