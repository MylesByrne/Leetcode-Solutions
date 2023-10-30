class Solution:
    def longestPalindrome(self, s: str) -> str:
        # abcded
        res = ""
        resLength = 0

        for i in range(len(s)):
            # odd
            r, l = i, i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if resLength < r - l + 1:
                    res = s[l:r+1]
                    resLength = r - l + 1
                r += 1
                l -= 1

            # even
            r, l = i + 1, i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if resLength < r - l + 1:
                    res = s[l:r+1]
                    resLength = r - l + 1
                r += 1
                l -= 1
        return res
