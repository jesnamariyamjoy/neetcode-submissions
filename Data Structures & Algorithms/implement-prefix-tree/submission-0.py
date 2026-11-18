class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class PrefixTree:

    def __init__(self):
        """
        Initializes the prefix tree object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the prefix tree.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the prefix tree, and false otherwise.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True