class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i, num in enumerate(nums):
            if num not in checked:
                checked[num] = i
            
            if target - num in checked:
                if i != checked[target - num]:
                    return [i, checked[target - num]]
            
