# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        i = 0
        while h != None:
            h = h.next
            i += 1
            
        l = 1
        
        if i % 2 == 0:
            while l < i/2 + 1:
                l = l + 1
                head = head.next
            return head
        if i % 2 == 1:
            while l < int(i/2) + 1:
                l = l + 1
                head = head.next
            return head
