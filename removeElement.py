class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        
        return(nums)

if __name__ == "__main__":
    soln=Solution()
    print(soln.removeElement([3,2,2,3],3))