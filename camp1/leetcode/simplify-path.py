class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        stack = []
        for idx in range(len(path)):
            if path[idx]:
                if path[idx] == "..":
                    if stack:
                        stack.pop()
                elif path[idx] != ".":
                    stack.append(path[idx])
        return "/"+"/".join(stack)
