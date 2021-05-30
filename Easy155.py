class MinStack(object):
    a = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        MinStack.a = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        MinStack.a.append(val)
    def pop(self):
        """
        :rtype: None
        """
        del MinStack.a[-1]

    def top(self):
        """
        :rtype: int
        """
        return MinStack.a[-1]

    def getMin(self):
        """
        :rtype: int
        """
        
        return min(MinStack.a)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()