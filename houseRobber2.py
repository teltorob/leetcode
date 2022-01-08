class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 0:
            return 0
        
        if length == 1:
            return nums[0]
        
        def helper(nums):
            prev, curr = 0, 0

            for num in nums:
                tmp = max(num + prev, curr)
                prev = curr
                curr = tmp

            return curr
        
        return max(helper(nums[: -1]), helper(nums[1:]))
