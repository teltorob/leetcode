class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Solved using binary search and two-pointers
        
        left, right = 0, len(arr) - 1
        res = []
        
        while(left <= right):
            mid = left + (right - left) // 2
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
                
        # Setting up pointers to be close to the element
        if mid == 0: 
            left = mid
            right = mid + 1
        else:
            left = mid - 1
            right = mid
            
        
        # Two pointers; Checks low and high doesn't exit bounds
        while k > 0 and left >= 0 and right < len(arr):
            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

            k -= 1
            
        # When left side is left and right is exhausted
        while k > 0 and left >= 0:
            res.append(arr[left])
            left -= 1
            k -= 1
            
        # When right side is left and left is exhausted
        while k > 0 and right < len(arr):
            res.append(arr[right])
            right += 1
            k -= 1

        return sorted(res)
