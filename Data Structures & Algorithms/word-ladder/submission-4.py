from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        visited={beginWord}
        connectedWords=defaultdict(list) #"#ko": [words,words]

        for word in wordList: #O(N)
            for index in range(len(word)): #O(A)
                variation=word[:index]+"#"+word[index+1:]
                connectedWords[variation].append(word)

        for index in range(len(beginWord)):
            variation=beginWord[:index]+"#"+beginWord[index+1:]
            connectedWords[variation].append(beginWord)

        deq=deque([(beginWord,1)])

        while deq:
            currentWord,length=deq.popleft()
            if currentWord==endWord:
                return length

            for index in range(len(currentWord)):
                variation=currentWord[:index]+"#"+currentWord[index+1:]
                for word in connectedWords[variation]:
                    if word not in visited:
                        deq.append([word,length+1])
                        visited.add(word)
                connectedWords[variation]=[]
        
        return 0



        """
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

        #EXAMINE EVERY POSSIBLE PATH #or we can do a bfs and the first time we hit the cell its valid 

        """



        