# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range (len(nums)-1): 
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False

                 # again indexing problem, i did it for len(nums) but when the last number arrives, the actual number is higher than the index, so it results to the number not existing so i did (len(nums)-1) instead of (len(nums))

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False    
