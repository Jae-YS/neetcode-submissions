class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/');
        stack = []
        print(split_path)
        for char in split_path:
            print(stack, "stack")
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "/" + "/".join(stack)
        
