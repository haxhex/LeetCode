from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        flag = 0
        f = head
        l_c=0
        def traverse(r,r_c):
            nonlocal flag
            nonlocal f
            nonlocal l_c
            if r is None:
                return 0
            traverse(r.next,r_c+1)
            
            if(f.val == r.val and l_c < r_c):
                f=f.next
                l_c+=1

            elif f.val != r.val and l_c < r_c:
                flag = 1                
        
        traverse(head,0)
        if(flag == 0):
            return True
        
        return False
    

print(Solution().isPalindrome([1, 2, 3, 2, 1]))