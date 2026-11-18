class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w
            
        ROWS, COLS = len(board), len(board[0])
        res = set()
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            curr_node = node.children[char]
            if curr_node.word:
                res.add(curr_node.word)
                # Optimization: Optional cleanup can be done, but setting word to None prevents duplicates
                curr_node.word = None 
                
            # Temporarily mark as visited
            board[r][c] = '#'
            
            # Explore neighbors: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
                    
            # Restore the cell
            board[r][c] = char
            
        # 2. Start DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return list(res)