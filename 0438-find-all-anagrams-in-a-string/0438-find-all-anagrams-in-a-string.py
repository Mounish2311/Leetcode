class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        freq_p = {}
        freq_window = {}

        for ch in p:
            freq_p[ch] = freq_p.get(ch, 0) + 1

        k = len(p)
        res = []

        for i in range(len(s)):
            freq_window[s[i]] = freq_window.get(s[i], 0) + 1

            if i >= k:
                left_char = s[i - k]
                freq_window[left_char] -= 1

                if freq_window[left_char] == 0:
                    del freq_window[left_char]

            if freq_window == freq_p:
                res.append(i - k + 1)

        return res