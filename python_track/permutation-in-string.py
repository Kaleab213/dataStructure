class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        i = 0
        j = len(s1)-1
        f_dict = {}
        s_dict = {}
        for k in s1:
            if k in f_dict:
                f_dict[k]+=1
            else:
                f_dict[k]=1
        for k in range(len(s1)):
            if s2[k] in s_dict:
                s_dict[s2[k]]+=1
            else:
                s_dict[s2[k]]=1
        
        while j < len(s2):
            if f_dict == s_dict:
                return True
            s_dict[s2[i]] -= 1
            if s_dict[s2[i]] == 0:
                del s_dict[s2[i]]
            i += 1
            j += 1
            if j < len(s2):
                if s2[j] in s_dict:
                    s_dict[s2[j]]+=1
                else:
                    s_dict[s2[j]] = 1 

        return False
