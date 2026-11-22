from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Collect all unique characters across all words
        adj = {ch: set() for word in words for ch in word}

        # Extract precedence edges from adjacent word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid if w1 is longer than w2 and w2 is a prefix of w1
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # True = currently in DFS path (visiting), False = completely processed (visited)
        visiting = {}
        order = []

        def dfs(ch: str) -> bool:
            if ch in visiting:
                return visiting[ch]  # True means cycle detected

            visiting[ch] = True
            for nxt in adj[ch]:
                if dfs(nxt):
                    return True
            visiting[ch] = False
            order.append(ch)
            return False

        for ch in adj:
            if ch not in visiting:
                if dfs(ch):
                    return ""

        order.reverse()
        return "".join(order)