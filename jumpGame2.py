class Solution:
    def jump(self, nums: List[int]) -> int:
        prev_max = curr_max = 0
        count = 0
        length = len(nums)
        
        
        for idx, val in enumerate(nums[:-1]): 
            curr_max = max((val + idx), curr_max)

            if (idx == prev_max):
                count += 1
                prev_max = curr_max
                
        return count
