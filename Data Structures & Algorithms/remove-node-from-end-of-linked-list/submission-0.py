# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        list_len = 0

        while curr:
            list_len += 1
            curr = curr.next

        target = list_len - n
        curr = head
        i = 0

        if target == 0:
            return curr.next

        while i < target - 1:
            curr = curr.next
            i += 1
        
        if not curr.next:
            curr.next = None
        else:
            curr.next = curr.next.next        

        return head


