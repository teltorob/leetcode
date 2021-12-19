class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0: return 0
        
        f, s, t = 0, 1, 1
        
        for _ in range(n-2):
            term = f + s + t
            f = s
            s = t
            t = term 
        return t
            