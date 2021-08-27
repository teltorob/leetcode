class Solution:
    def removeDuplicates(self, nums) -> int:
        nums[:]=list(dict.fromkeys(nums))
        print(nums)
        

if __name__ == "__main__":
    soln=Solution()
    soln.removeDuplicates([-1,0,0,0,0,3,3])