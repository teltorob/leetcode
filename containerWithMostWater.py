class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        def area(left, right):
            b = right - left
            h = min(height[left], height[right])
            
            a = b * h
            
            return a
        
        while (left < right):
            max_area = max(max_area, area(left, right))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
                
        