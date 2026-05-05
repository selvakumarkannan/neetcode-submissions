class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        resp = []

        bucket = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)

        for num, count in hashmap.items():
            bucket[count].append(num)

        for nums in range(len(bucket)-1, 0, -1):
            for num in bucket[nums]:
                resp.append(num)
                if len(resp) == k:
                    return resp
