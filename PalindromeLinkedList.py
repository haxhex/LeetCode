# A Linked Lisy Node
from unittest import result


class Node:
    # Node constructor just have data and point to next node (a pointrer)
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
# check nodes from left and right to check if Palindrome or not        
def checkPalindrome(left, right):
    # base case
    # consider none of nodes are remind
    # end of the nodes
    if right is None:
        return True, left
    
    # consider moving from left to right
    # so the next node would be the right node
    val, left = checkPalindrome(left, right = next)
    
    # the result is true when left data is equal to right data
    result = val and (left.data == right.data)
    
    # move the pointer from left
    left = left.next
    
    # left just use when see all nodes (ath the end of array)
    return result, left
    
# func to check the linked list is a palindrome pr not
def checkPlain(head):
    return checkPalindrome(head, head)[0]

if __name__ == '__main__':
    
    # input keys
    keys = [1, 3, 5, 3, 1] # True
    
    head = None
    
    for i in  reversed(range(len(keys))):
        head = Node(keys[i], head)
        
    if checkPlain(head):
        print("is palindrome")
    else:
        print("not palindrome")


