class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = int(str(x_abs)[::-1])
        return rev * sign if -(2**31) <= rev * sign <= 2**31 - 1 else 0
