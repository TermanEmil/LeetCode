romans = {
    'I': 1,
    'V': 5,
    
    'X': 10,
    'L': 50,
    
    'C': 100,
    'D': 500,
    
    'M': 1000,
    
    'IV': 4,
    'IX': 9,
    
    'XL': 40,
    'XC': 90,
    
    'CD': 400,
    'CM': 900,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        i = 0
        while i < len(s):
            val = romans.get(s[i:i+2], None)
            
            if val:
                result += val
                i += 2
            else:
                result += romans[s[i]]
                i += 1

        return result
