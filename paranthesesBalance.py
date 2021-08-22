class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        parMap={
            ']':'[',
            '}':'{',
            ')':'(',
        }
        stack=[]
        revPts=[']','}',')']
        for char in s:
            
            if char not in revPts:
                stack.append(char)
                
            elif (char in revPts) and not (stack):
                return False
            
            else:
                if stack.pop() != parMap[char]:
                    return False
        if(stack):
            return False

        return True

    
if __name__ == "__main__":
    soln=Solution()
    print(soln.isValid('('))