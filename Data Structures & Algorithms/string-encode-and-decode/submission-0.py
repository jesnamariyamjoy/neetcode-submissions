class Solution:
    def encode(self, strs: List[str]) -> str:
        # For each string, append its length, a delimiter '#', and the string itself
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Parse the encoded string using pointers
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of the delimiter '#'
            while s[j] != '#':
                j += 1
            # Extract the length of the upcoming string
            length = int(s[i:j])
            # Extract the string using the length
            res.append(s[j + 1 : j + 1 + length])
            # Move pointer `i` past the current decoded string
            i = j + 1 + length
        return res