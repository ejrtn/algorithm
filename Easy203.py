# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is not None:
            if head.next is not None:
                if head.val == val:
                    head = head.next
                    head = self.removeElements(head,val)
                else:
                    head.next = self.removeElements(head.next,val)
            else:
                if head.val == val:
                    head = head.next
        return head