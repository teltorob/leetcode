class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # This solution uses my logic from maximum subarray (sum). 
        curr_max = curr_min = prev_max = maximum = nums[0]
        
        for num in nums[1:]:     
            curr_max = max(num, num * curr_max, curr_min * num)     # curr_min * num handles the case of two -ves resulting positive
            curr_min = min(num, num * curr_min, num * prev_max)      # num * minimum handles the case where -ve and +ve result in negative
            prev_max = curr_max                                     # stores the value of previous max throughout an interation
            
            maximum = max(curr_max, maximum)
            
            
        return maximum
