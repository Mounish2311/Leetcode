class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = max(nums)
        second = -1

        for num in nums:
            if num != largest:
                second = max(second, num)

        if largest >= 2 * second:
            return nums.index(largest)

        return -1
