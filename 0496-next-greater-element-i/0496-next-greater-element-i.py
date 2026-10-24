class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for num in nums1:
            found = False

            for i in range(len(nums2)):
                if nums2[i] == num:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > num:
                            result.append(nums2[j])
                            found = True
                            break
                    break

            if not found:
                result.append(-1)

        return result