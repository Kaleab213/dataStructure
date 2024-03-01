class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def recursive(hs):
            if len(hs)<2:
                return ""

            badstr = False
            for idx in range(len(hs)):
                if hs[idx].isupper() and hs[idx].lower() in hs:
                    continue
                if hs[idx].islower() and hs[idx].upper() in hs:
                    continue
                else:
                    badstr = True
                    break
            
            if badstr:
                left = recursive(hs[:idx])
                right = recursive(hs[idx+1:])
                if len(left)>=len(right):
                    return left
                return right
            else:
                return hs
                
        return recursive(s)