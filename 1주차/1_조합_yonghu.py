class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(start, comb, depth):
            if depth == k:
                result.append(comb[:])
            for i in range(start, n+1):
                comb.append(i)
                dfs(i+1, comb, depth+1)
                comb.pop()
        dfs(1, [], 0)
        return result
