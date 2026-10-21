class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result