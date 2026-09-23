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
        ref=self.check(word)
        return ref.string==word if ref else False
        

    def startsWith(self, prefix: str) -> bool:
        ref=self.check(prefix)
        return ref is not None

    def check(self,prefix):
        reference=self.prefix
        for w in prefix:
            if w not in reference.adj:
                return None
            reference=reference.adj[w]
        return reference


        
        