class Solution:

    def sortedSquares(self, nums):
        right = 0
        
        numSize=len(nums)-1 
        
        while right <= numSize and nums[right] < 0:
            right+=1
        
        left = right -1
        res=[]
        
        while right <= numSize and left>=0:
            sqL = nums[left]**2
            sqR = nums[right]**2
            
            
            if sqR > sqL:
                res.append(sqL)
                left -=1
                
            else:
                res.append(sqR)
                right +=1
        
        while right <= numSize:
            sqR = nums[right]**2
            res.append(sqR)
            right +=1
                
        while left >=0:
            sqL = nums[left]**2
            res.append(sqL)
            left -=1
            
        
        return res
            
                
if __name__ == "__main__":
    soln=Solution()
    print(soln.sortedSquares([-4,-1,0,3,10])) 
