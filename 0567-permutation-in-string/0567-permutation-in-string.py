class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}

        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1

        k = len(s1)

        for i in range(len(s2)):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1

            if i >= k:
                left_char = s2[i - k]
                freq2[left_char] -= 1

                if freq2[left_char] == 0:
                    del freq2[left_char]

            if freq1 == freq2:
                return True

        return False