class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dist = {}

        for i in range(len(nums)):
            t = target-nums[i]
            if t in dist:
                return [dist[t], i]
            dist[nums[i]] = i
        return
        