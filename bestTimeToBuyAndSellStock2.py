class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum, prev = 0, prices[0]
        
        for i in range(1, len(prices)):
            maximum += max(0, prices[i] - prev)     # If loss is incurred it will add 0 else the profit
            prev = prices[i]
            
        return maximum
