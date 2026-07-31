class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use a dictionary
        if len(s)!=len(t):
            return False
        dictS,dictT = {},{}
        for i in s:
            if i not in dictS:
                dictS[i]=1
            else:
                dictS[i]+=1
        for i in t:
            if i not in dictT:
                dictT[i]=1
            else:
                dictT[i]+=1

        for i in dictT:

            if i in dictS:
                if dictT[i]!=dictS[i]:
                    return False
            else: 
                return False
        return True

        




