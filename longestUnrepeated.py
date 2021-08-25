class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0

        maximum=0
        memo=set()

        for end,val in enumerate(s):
            
            if val in memo:
                while (start<end):
                    if(s[start]==val): 
                        start+=1
                        break
                    else:
                        memo.remove(s[start])
                        start+=1
            else:
                memo.add(val)
            
            maximum=max(maximum,(end-start+1))

        return maximum


    
if __name__ =='__main__':
    soln=Solution()
    print(soln.lengthOfLongestSubstring("abcabcbb"))