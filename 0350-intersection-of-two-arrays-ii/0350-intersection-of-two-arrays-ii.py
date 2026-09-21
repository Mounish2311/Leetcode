class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        res = []

        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1

        return res
