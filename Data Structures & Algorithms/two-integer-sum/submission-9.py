class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the index of nums elements that sums up to target
        # ofc you can do it by using a nested for loop
        # but dict is a better choice
        # try solving it using brute force first
        prevMap ={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i


        

            
        