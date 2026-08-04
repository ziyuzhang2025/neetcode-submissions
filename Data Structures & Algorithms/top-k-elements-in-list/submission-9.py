class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #creating the dict with number and count
    # the create the array with number of columns equal to the number of elements
        count = {}
        table = [[] for _ in range(len(nums)+1)]
        #note that the result we not using []*(len(nums)-1)is because list is mutable, if we do that all lists refer to the same changable list
        for i in nums:
            count[i]= 1+ count.get(i,0)
        # now weve stored the numbers and corresponding count into the dict
        # what we need to do now is put them into the array
        for i,c in count.items():
            table[c].append(i)
        #now we pushed all the integers into the coresponding column 
        res =[]
        for i in range(len(table)-1,0,-1):
            for c in table[i]:
                res.append(c)
            if len(res)==k:
                return res