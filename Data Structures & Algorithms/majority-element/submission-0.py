import random 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            selectedNumber = random.choice(nums)
            if nums.count(selectedNumber) > n //2:
                return selectedNumber
        