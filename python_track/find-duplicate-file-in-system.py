class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for path in paths:
            path = path.split()
            parent_file = path[0]
            for i in range(1, len(path)):
                file_name, content = path[i].split("(")
                (mydict[content]).append(parent_file+"/"+file_name)

        res = []
        for content in mydict:
            if len(mydict[content])>1:
                res.append(mydict[content])
        return res
