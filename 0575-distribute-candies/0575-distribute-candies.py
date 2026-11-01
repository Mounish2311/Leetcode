class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        freq = {}

        for candy in candyType:
            freq[candy] = 1

        return min(len(freq), len(candyType) // 2)