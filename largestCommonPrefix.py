class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==1:
            return strs[0]
        
        itr= zip(*strs)
        res=''
        for *char, in itr:
            char=list(set(char))
            if len(char)==1:
                res+=char[0]
            else:
                break
 
        return(res)

if __name__ == "__main__":
    soln=Solution()
    print(soln.longestCommonPrefix(["flower","flow","flown"]))