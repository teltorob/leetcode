class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        greatest = max(nums)
        ls = [0] * (greatest + 1)
        
        for num in nums:        # Calculates the sum of all the occurances of the number
            ls[num] += num 
            
        prev = curr = 0
        
        for l in ls:            # Uses House Robber dynamic strategy to maximise the output
            prev, curr = curr, max(prev + l, curr)
            
        return curr
