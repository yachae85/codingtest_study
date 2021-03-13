import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = collections.Counter(s)
        seen = set()
        for char in s:
            count[char] -= 1
            if char in seen:
                continue

            while stack and stack[-1] > char and count[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)
        return ''.join(stack)
