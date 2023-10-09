"""Leetcode Problem #2156 --> Find Substring with Given Hash Value"""

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        power_factor = pow(power, k-1, modulo)
        
        rolling_hash = 0 
        matching_index = -1 
        
        for i, ch in enumerate(reversed(s)): 
            if i >= k: 
                rolling_hash -= (ord(s[len(s) - i + k - 1]) - ord('a') + 1) * power_factor
            rolling_hash = (rolling_hash * power + (ord(ch) - ord('a') + 1)) % modulo
            
            if i >= k-1 and rolling_hash == hashValue: 
                matching_index = len(s) - i - 1
        
        if matching_index != -1:
            return s[matching_index: matching_index + k]
        return ""
