class Solution(object):
    def generate(self, rowIndex):
        
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        result = []
        for i in range(rowIndex+1):
            arr=[]
            if i==0:
                arr.append(1)
                result.append(arr)
            elif i==1:
                arr.append(1)
                arr.append(1)
                result.append(arr)
            else:
                arr.append(1)
                print(len(result[i-1]))
                for x in range(len(result[i-1])-1):
                    arr.append(result[i-1][x]+result[i-1][x+1])
                arr.append(1)
                result.append(arr)
        
        return result[len(result)-1]
		

s = Solution()
print(s.generate(3))

