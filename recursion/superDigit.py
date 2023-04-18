#!/usr/bin/python3


class Solution:
    def superDigit(self, n: int, k: int):
        _number = str(n) * k
        
        def calculateSuperDigit(n: str) -> int:
            if len(n) == 1:
                return int(n)
            print(sum(list(map(int, n))))

        calculateSuperDigit(_number)


sol = Solution()
print(sol.superDigit(123, 3))
