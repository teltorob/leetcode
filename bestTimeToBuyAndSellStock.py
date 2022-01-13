class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum, prev = 0, prices[0]
        
        for i in range(1, len(prices)):
            maximum = max(maximum, prices[i] - prev)
            prev = min(prev, prices[i])
            
        return maximum
