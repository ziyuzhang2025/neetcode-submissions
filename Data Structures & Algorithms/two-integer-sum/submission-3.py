class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the index of nums elements that sums up to target
        # ofc you can do it by using a nested for loop
        # but dict is a better choice
        # try solving it using brute force first
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        

            
        