class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ={char:i for i, char in enumerate(s)}
        stack=[]
        visited=set()
        for i, char in enumerate(s):
            if char in visited:continue
            while stack and stack[-1]>char and last_occ[stack[-1]]>i:
                removed=stack.pop()
                visited.remove(removed)
            stack.append(char)
            visited.add(char)
        return "".join(stack)