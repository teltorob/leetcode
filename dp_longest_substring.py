class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp_arr = [[0] * len(s) for _ in range(len(s))]
        res = s[0]
        res_len = 1
                
        for i in range(length):
            dp_arr[i][i] = 1
        
        #main loop to fill up 0 or 1 using dynamically to the upper half of the matrix
        for i in range(1, length):
            left = 0
            for right in range (i, length):
                #if the outer (start and end) char are the same AND the inner string is palindromic , start + inner + end is also palandromic
                if s[left] == s[right]:
                    if (right - left) ==1 or dp_arr[left + 1][right-1] == 1:
                        dp_arr[left][right] = 1
                        
                        l = right - left + 1 
                        if l > res_len:
                            res = s[left : right + 1]
                            res_len = l
                else:
                    dp_arr[left][right] = 0
                left += 1

        return res
            


