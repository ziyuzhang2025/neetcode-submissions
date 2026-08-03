class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the index of nums elements that sums up to target
        # ofc you can do it by using a nested for loop
        # but dict is a better choice
        # try solving it using brute force first
        # next method to try is sorting
        A = []
        for i,n in enumerate(nums):
            A.append([n,i])

        A.sort()
        i,j=0,len(nums)-1
        while A[i][0]+A[j][0]!=target and i<j:
            if A[i][0]+A[j][0]>target:
                j-=1
            else:
                i+=1
        return [min (A[i][1],A[j][1]),max(A[i][1],A[j][1])]


