class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        zero = 0
        for n in nums:
            if n == 0:
                zero += 1
            else:
                total *= n
        if zero > 1:
            return [0]*len(nums)
        if zero == 1:
            for n in nums:
                if n != 0:
                    res.append(0)
                else:
                    res.append(int(total))
            return res

        for n in nums:
            if n == 0:
                res.append(0)
            else:
                res.append(int(total/n))
        return res