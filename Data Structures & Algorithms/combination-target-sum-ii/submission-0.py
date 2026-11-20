class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicate values at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates is sorted, no subsequent element can fit
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return res