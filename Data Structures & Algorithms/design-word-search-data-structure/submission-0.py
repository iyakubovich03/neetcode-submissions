class Node:
    def __init__(self):
        self.nextCharacter={}
        self.isWord=False

class WordDictionary:

    def __init__(self):
        self.start=Node()

        

    def addWord(self, word: str) -> None:
        reference=self.start

        for w in word:
            if w not in reference.nextCharacter:
                reference.nextCharacter[w]=Node()
            reference=reference.nextCharacter[w]

        reference.isWord=True
        

    def search(self, word: str) -> bool:

        def dfs(index,reference):
            if index==len(word) and reference.isWord:
                return True#good case need theh false case as well 
            elif index==len(word):
                return False

            currentCharacter=word[index]

            if currentCharacter!="." and currentCharacter not in reference.nextCharacter:
                return False
            
            value=False

            if currentCharacter in reference.nextCharacter:
                value=dfs(index+1,reference.nextCharacter[currentCharacter])
            elif currentCharacter==".":
                for key in reference.nextCharacter:
                    value=dfs(index+1,reference.nextCharacter[key])
                    if value:
                        return True

            return value
        return dfs(0,self.start)


        
#worst case just iterate   