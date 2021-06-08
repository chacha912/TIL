class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    def reverse(node, prev=None):
        if not node:
            return prev

        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

head = [1,2,2,1]
print(isPalindrome(head))