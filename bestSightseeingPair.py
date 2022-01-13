class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maximum, prev = 0, values[0]
        
        for idx in range(1, len(values)):
            maximum = max(maximum, prev + values[idx] - idx)    # Comes early in order to ensure it doesn't miss the prec high + new high
            prev = max(prev, values[idx] + idx)                 # Maximum value deicovered yet
            
        return maximum
