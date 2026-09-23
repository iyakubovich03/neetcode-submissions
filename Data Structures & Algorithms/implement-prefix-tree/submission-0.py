class Node:
    def __init__(self):
        self.adj={}
        self.string=""


class PrefixTree:

    def __init__(self):
        self.prefix=Node()
        

    def insert(self, word: str) -> None:
        reference=self.prefix
        for w in word:
            if w not in reference.adj:
                reference.adj[w]=Node()
            reference=reference.adj[w]
        reference.string=word



    def search(self, word: str) -> bool:
        reference=self.prefix
        for w in word:
            if w not in reference.adj:
                return False
            reference=reference.adj[w]
        return reference.string==word
        

    def startsWith(self, prefix: str) -> bool:
        reference=self.prefix
        for w in prefix:
            if w not in reference.adj:
                return False
            reference=reference.adj[w]
        return True

        
        