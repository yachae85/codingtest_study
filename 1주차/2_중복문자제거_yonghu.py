import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = collections.Counter(s)
        seen = set()
        for c in s:
            count[c] -= 1
            if c in seen:
                continue

            while stack and stack[-1] > char and count[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)
        return ''.join(stack)
