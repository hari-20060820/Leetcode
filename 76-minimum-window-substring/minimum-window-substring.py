from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Frequency of characters required
        need = Counter(t)

        # Frequency of characters in current window
        window = {}

        have = 0
        needCount = len(need)

        left = 0
        res = [-1, -1]
        resLen = float("inf")

        for right in range(len(s)):

            # Expand the window
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Check if this character's required count is satisfied
            if c in need and window[c] == need[c]:
                have += 1

            # Try shrinking while window is valid
            while have == needCount:

                # Update minimum window
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Remove left character
                window[s[left]] -= 1

                # If requirement is broken
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""