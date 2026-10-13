from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited=set()
        connectedWords=defaultdict(list) #"#ko": [words,words]

        for word in wordList:
            for index in range(len(word)):
                variation=word[:index]+"#"+word[index+1:]
                connectedWords[variation].append(word)

        for index in range(len(beginWord)):
            variation=beginWord[:index]+"#"+beginWord[index+1:]
            connectedWords[variation].append(beginWord)

        print(connectedWords)

        memo={}
        def dfs(currentWord):
            print(f" we are at {currentWord}")
            if currentWord in memo:
                return memo[currentWord]

            if currentWord==endWord:
                return 1

            minValue=float('inf')
            visited.add(currentWord)

            for index in range(len(currentWord)):
                variation=currentWord[:index]+"#"+currentWord[index+1:]
               
                for word in connectedWords[variation]:
                    print(f"looking at connected word {word}")
                    if word not in visited:
                        minValue=min(minValue,dfs(word))
                        print(f"current min value {minValue}")

            visited.remove(currentWord)
            memo[currentWord]=minValue+1

            return memo[currentWord]

        value=dfs(beginWord)
        return value if value!=float('inf') else 0



        



        