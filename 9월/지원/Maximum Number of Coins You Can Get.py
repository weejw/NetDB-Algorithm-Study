class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles,reverse=True)[:int(len(piles)*2/3)]
        res = 0
        for i in range(1, len(piles), 2):
            res += piles[i]
        
        return res