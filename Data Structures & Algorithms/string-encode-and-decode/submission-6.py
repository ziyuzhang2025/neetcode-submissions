class Solution:

    def encode(self, strs: List[str]) -> str:
        # use non ascii character as a delimiter
        # we need to encode the str
        res = ""
        for s in strs:
            count= str(len(s))

            res+=count+"#"+s
        return res



    def decode(self, s: str) -> List[str]:
        
        # now we need to identify the number, get the number 
        # identify the indices of strs 
        # retrun the orginal code
        res =[]
        #now we have the res list that needs to be returned later
        # what we need to do now is to append the strs into the res
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
