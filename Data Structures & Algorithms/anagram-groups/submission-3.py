class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary to store all the distinct elements 
        store = {}
        for i in strs:
            if str(sorted(i)) not in store:
                store[str(sorted(i))]=[i]
            else:
                store[str(sorted(i))].append(i)
        ans =[]
        for key in store:
            ans.append(store[key])

        
        return ans
