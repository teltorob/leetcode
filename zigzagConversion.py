class Solution:
    def convert(self, s: str, numRows: int) -> str:
        gap= numRows-2
        sLen= len(s)
        step = 2*(numRows-1)
        
        res=''
        if sLen<=1 or numRows==1:
            return s
        for row in range(numRows):
            isEndRow= (row==0 or row==numRows-1)
            diag=2*(numRows-(row+1))
            itr=0
            for pos in range (row,sLen, step):
                    
                res+= s[pos]
                if (not (isEndRow) and (pos+diag<sLen)):
                    res+=s[pos+diag]
                    
                itr+=1
                
        
        return res

if __name__ == "__main__":
    soln=Solution()
    print(soln.convert("PAYPALISHIRING",3))

    #  PAHNAPLSIIGYIR  is the expected output