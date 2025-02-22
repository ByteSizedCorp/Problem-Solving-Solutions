class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        count_dict = {}

        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        for key, value in count_dict.items():
            buckets[value].append(key)

        result = []

        for i in range(len(buckets)-1, 0, -1):
            for item in buckets[i]:
                result.append(item)
                if(len(result) == k):
                    return result