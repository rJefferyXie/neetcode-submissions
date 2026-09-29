class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for idx, n in enumerate(nums):
            if target - n in sums:
                return [sums[target - n], idx]
            sums[n] = idx