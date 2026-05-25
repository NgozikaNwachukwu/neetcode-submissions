class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
    # Python cuts the string at every single "/".
    # - It looks to the LEFT of each slash to grab an item.
    # - Consecutive slashes (like "//") leave "nothing" to the left, creating empty strings ('').
    # - The very last item is whatever is left over at the end of the string.
    # Example: "/..//_home/" becomes ['', '..', '', '_home', '']
        paths = path.split("/")

        for word in paths:
            if word == "..":
                if len(stack) != 0:
                    stack.pop()
            elif word != "" and word != ".":
                stack.append(word)
        

        final = "/" + "/".join(stack)
        return final
        