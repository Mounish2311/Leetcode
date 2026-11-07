class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        count = 1
        maximum = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1

            maximum = max(maximum, count)

        return maximum