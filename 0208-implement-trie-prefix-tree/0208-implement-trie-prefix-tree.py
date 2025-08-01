class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node:
                return False
            node = node[i]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)