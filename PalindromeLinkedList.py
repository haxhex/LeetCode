
# A linkesd list Node
from django.urls import Resolver404


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# Rec func tgo check a palindrome or not
def checkPalindrome(left, right):
    if right is None:
        return True, left
    val, left = checkPalindrome(left, right.next)
    result = val and (left.data == right.data)
    left = left.next 
    return result, left
def checkPalin(head):
    return checkPalindrome(head, head)[0]

if __name__ == '__main__':
    #input keys
    keys = [1, 3, 5, 3, 1]
    head = None
    for i in reversed(range(len(keys))):\
        head = Node(keys[i], head)
    
    if (c)
        