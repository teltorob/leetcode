class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        
        # Self
        # for i in range(length - 3, -1, -1):
        #     cost[i] += min(cost[i + 1], cost[i + 2])
        # return min(cost[0], cost[1])
        
        
        # Found in discussion
        for i in range(2, length):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[length-1], cost[length-2])