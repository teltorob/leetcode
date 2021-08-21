class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen=len(s)
        
        if sLen==1:
            return s
        
        if sLen>1:
            firstPos=0
            secondPos=0
            
            pal=''
            
            targetChar=''
            
            maxLen=0
            longestString=''
            
            for index,targetChar in enumerate (s): 
                tempS=s
                while(tempS.rfind(targetChar)!=-1):
                    secondPos=tempS.rfind(targetChar)
                    pal=tempS[index:secondPos+1]
                
                    lp=len(pal)
                    q,r= divmod(lp,2)


                    if pal[0:q+r]==pal[q:][::-1]:
                        if len(pal)>maxLen:
                            maxLen=len(pal)
                            longestString=pal
                            break

                    tempS=tempS[:secondPos]
                if(maxLen>(sLen-index)):
                    break
            return(longestString)
                    
            

if __name__ == "__main__":
    soln=Solution()

    solution=soln.longestPalindrome('babad')
    print(solution)