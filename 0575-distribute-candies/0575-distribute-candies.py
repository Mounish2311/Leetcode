class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique = len(set(candyType))
        return min(unique, len(candyType) // 2)