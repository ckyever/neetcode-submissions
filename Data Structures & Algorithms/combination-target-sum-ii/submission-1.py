class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(combo: List[int], index: int, total: int):
            if total == target:
                result.append(combo.copy())
                return
            
            if total > target or index >= len(candidates):
                return

            # Add current candidate then increment index
            # Add nothing increment index until new number
            candidate = candidates[index]
            combo.append(candidate)
            dfs(combo, index+1, total + candidate)
            combo.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(combo, index+1, total)


        dfs([], 0, 0)
        return result
                