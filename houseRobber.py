class Solution:
    def rob(self, nums: List[int]) -> int:
        
       # Self 
        length = len(nums)
        
        
        for i in range(2, length):
            if i - 3 < 0:
                nums[i] += nums[i - 2]
                continue
                
            nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[length - 1], nums[length - 2])
    
    
    
# Soln taken from discussion section

#             prev, curr = 0, 0

#             for num in nums:
#                 tmp = max(num + prev, curr)
#                 prev = curr
#                 curr = tmp

#             return curr
    
    
