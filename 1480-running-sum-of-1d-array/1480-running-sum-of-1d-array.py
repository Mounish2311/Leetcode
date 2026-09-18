class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        return prefix[1:]