class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1 
        majorityelement = (len(nums))/2
        nums.sort()
        if len(nums) == 1:
                return nums[0]
        for i in range(len(nums) - 1 ):
            if nums[i] == nums[i+1]:
                count+=1
                if count > majorityelement:
                   return nums[i]
            elif nums[i] != nums[i+1]: 
                count = 1
