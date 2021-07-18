# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        
        r = None
        if head is not None:
            r = ListNode(head.val,None)
            head = head.next
        else:
            return r
        
        
        while(True):
            if head is not None:
                r = ListNode(head.val,r)
                head = head.next
            else:
                return r