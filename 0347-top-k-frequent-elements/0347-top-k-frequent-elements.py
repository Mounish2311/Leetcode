class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        res = []

        for i in range(k):
            res.append(sorted_items[i][0])

        return res