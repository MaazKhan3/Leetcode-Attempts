class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        sign = 1
        result = 0

        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        result = result * sign

        MIN = -2**31
        MAX = 2**31 -1

        if result < MIN:
            return MIN
        if result > MAX:
            return MAX

        return result
        