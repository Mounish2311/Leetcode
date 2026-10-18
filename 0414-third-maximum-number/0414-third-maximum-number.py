class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse=True)

        if len(nums) >= 3:
            return nums[2]

        return nums[0]