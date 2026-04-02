class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(2 ** len(nums)):
            mask = bin(i)[2:]
            mask = list(mask)
            temp = []
            
            while len(mask) < len(nums):
                mask = ['0'] + mask

            for j in range(len(mask)):
                if mask[j] == '1':
                    temp.append(nums[j])

            res.append(temp)
        return res
            