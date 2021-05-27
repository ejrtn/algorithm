# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        v = head
        a = []
        pos = -1
        while(True):
            if v is None:
                return False
            a.append(v.val)
            
            # print(a)
            v = v.next
            if v is not None:
                for i in range(len(a)):
                    # print(v.val==a[i],v.val,a[i])
                    if v.val == a[i]:
                        for x in range(i,len(a)):
                            if x == len(a)-1:
                                if v.next is not None:
                                    v = v.next
                                    # print("result",v.val==a[i],v.val,a[i])
                                    if v.val == a[i]:
                                        return True
                                else:
                                    return False
                            if v.val != a[x]:
                                break
                            v = v.next
        return True