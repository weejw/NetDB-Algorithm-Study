class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        while True:
            for i in range(idx+1, len(nums)):
                if nums[idx] + nums[i] == target:
                    return [i, idx]
            idx += 1
