class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        c = 0
        digits[0] += 1

        for i in range(len(digits)):
            digits[i] += c
            if digits[i] >= 10:
                c = 1
                digits[i] = digits[i] % 10
            else:
                c = 0
                break
        if c == 1:
            digits.append(1)
        
        return digits[::-1]