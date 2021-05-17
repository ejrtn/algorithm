class Solution(object):
    def generate(self, numRows):
        
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        result = []
        for i in range(numRows):
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
                for x in range(len(result[i-1])-1):
                    arr.append(result[i-1][x]+result[i-1][x+1])
                arr.append(1)
                result.append(arr)
        
        return result
		

