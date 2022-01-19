class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
    
        for i, val in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            
            if val > 0:
                break
                
            if i != 0 and nums[i-1] == val:
                continue
            
            while (left < right):
                left_num = nums[left]
                right_num = nums[right]
                curr_sum = val + left_num + right_num
                triplet = [val, left_num, right_num]
                
                if (curr_sum) == 0 and triplet not in res:
                    res.append(triplet)
                    left += 1
                    right -= 1
                    
                elif (curr_sum) > 0:
                    right -= 1
                else:
                    left += 1
                    
        return res
                    
