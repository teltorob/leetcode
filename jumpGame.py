class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum: int = 0
            
        for idx, val in enumerate(nums):            # Maximum number of steps possible until idx
            if (idx > maximum):                     # If maximum number of steps until that index is                                                           less than index
                return False
            
            maximum = max((val + idx), maximum)     # Val + Idx gives you maximum number of steps fwd
        return True
