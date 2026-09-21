class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        res=[]
        for num in s1:
            if num in s2:
                res.append(num)
        return res