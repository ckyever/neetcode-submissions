class Solution:
    def combo_to_freq_key(self, combo: List[int]) -> str:
        key = [0] * 50

        for num in combo:
            key[num-1] += 1
        
        return "".join([str(num) for num in key])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = {}

        def dfs(combo: List[int], index: int, total: int):
            if total == target:
                key = self.combo_to_freq_key(combo)
                if key not in result:
                    result[key] = combo.copy()
                return
            
            if total > target or index >= len(candidates):
                return

            candidate = candidates[index]
            index += 1
            dfs(combo.copy(), index, total)
            combo.append(candidate)
            dfs(combo.copy(), index, total + candidate)

        dfs([], 0, 0)
        return [combo for combo in result.values()]
                