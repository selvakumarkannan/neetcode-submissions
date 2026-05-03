class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = {}
        for i,n in (enumerate(nums)):
            difference = target - nums[i] 
            print(difference)
            if (difference in final):
                secondIndex = final[difference]
                return [secondIndex, i ]
            final[n]= i
            
                


        