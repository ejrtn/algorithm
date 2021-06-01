class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        
        while(True):
            if i >= len(numbers)-1:
                return []
            for x in range(i+1,len(numbers)):
                
                if numbers[i] + numbers[x] == target:
                    return [i+1,x+1]
                if numbers[x] > target - numbers[i]:
                    
                    break
                if numbers[i] == numbers[x]:
                    i = x
            i += 1