class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Self thought code, also found it is known as Kadane's Algorithm
        maximum = curr_max = nums[0]
        
        for num in nums[1:]:
            curr_max = max(num, num + curr_max)     # This will replace smaller sum by val, if val>sum
            maximum = max(maximum, curr_max)
            
        return maximum
