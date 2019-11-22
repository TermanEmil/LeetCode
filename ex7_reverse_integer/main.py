class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x *= -1
            sign = -1
        else:
            sign = 1
        
        result = 0
        while x:
            result = result * 10 + x % 10
            x = x // 10
        
        # Overflow???....
        if result >= 2147483648:
            print(result)
            return 0
        
        return result * sign
