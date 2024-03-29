class Solution:
    def isValid(self, s: str) -> bool:
        newArray = []
        for i in range(len(s)):
            if s[i] == "(":
                newArray.append(s[i])
            elif s[i] == "[":
                newArray.append(s[i])
            elif s[i] == "{":
                newArray.append(s[i])
            elif s[i] == ")":
                if len(newArray) == 0:
                    return False
                elif newArray[-1] == "(":
                    newArray.pop()
                else:
                    return False
            elif s[i] == "]":
                if len(newArray) == 0:
                    return False
                elif newArray[-1] == "[":
                    newArray.pop()
                else:
                    return False
            elif s[i] == "}":
                if len(newArray) == 0:
                    return False
                elif newArray[-1] == "{":
                    newArray.pop()
                else:
                    return False
        if len(newArray) == 0:
            return True
        else:
            return False
    