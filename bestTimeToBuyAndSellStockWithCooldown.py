class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Code picked up from discussion section
        sold = 0
        hold = -sys.maxsize
        cool = 0
        for price in prices:
            sold_tmp = sold
            sold = max(sold, hold + price)
            hold = max(hold, cool - price)
            cool = sold_tmp
        return sold
