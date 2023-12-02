class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for i in range(len(command)):
            if command[i]=="G":
                res+="G"
            elif command[i]=="(":
                if command[i+1]==")":
                    res += "o"
                else:
                    res += "al"
        return res



        