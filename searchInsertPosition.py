class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while (left<=right):
            mid = left + (right-left)//2
            current = nums[mid]
            
            if current==target:
                return mid
            elif current < target:
                left= mid+ 1
            else:
                right= mid-1
                
        return left

if __name__ == "__main__":
    soln=Solution()
    print(soln.searchInsert([1,3,5,6], 7)) # Answer : 4