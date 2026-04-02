class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = sorted(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        s = []
        while self.nums and self.nums[-1] > val:
            s.append(self.nums.pop())
        
        
        self.nums.append(val)
        while s:
            self.nums.append(s.pop())
        return self.nums[-self.k]

