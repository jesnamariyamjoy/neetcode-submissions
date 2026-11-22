from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        m = len(beginWord)
        pattern_map = defaultdict(list)

        # Build wildcard buckets for words in wordList
        for word in word_set:
            for i in range(m):
                pattern = f"{word[:i]}*{word[i + 1:]}"
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            curr_word, length = queue.popleft()

            for i in range(m):
                pattern = f"{curr_word[:i]}*{curr_word[i + 1:]}"

                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return length + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))

                # Optional: clear list after exploring so the same pattern isn't re-scanned
                pattern_map[pattern].clear()

        return 0