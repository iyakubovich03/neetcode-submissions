class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:


        tickets.sort()
        result=[]
        adjList=defaultdict(list)
        neededTickets=defaultdict(int)
        usedTickets=defaultdict(int)
        for source,target in tickets:
            adjList[source].append(target)
            neededTickets[(source,target)]+=1

        def dfs(current):
            for child in adjList[current]:
                if usedTickets[(current,child)]<neededTickets[(current,child)]:
                    usedTickets[(current,child)]+=1
                    dfs(child)
            result.append(current)
        dfs("JFK")
        return result[::-1]
        """
        adjacenyList={source:[children]} #O(N)
        tickets={destination:#frequency}#O(N)
        ticketsUsed={}#O(n)
        result=[]
        current=[]
        #compelx
        def dfs(current):
            if tickets==ticketsUsed:
                result.append(current.copy)
                return

            for chilren in adjacenlyList[current]:
                if ticketsUsed[children]<used[tikcets]:
                    ticektsUSed[chidle]+=1
                    current.append(chilren)
                    dfs(child)
                    ticektsUSed[chidle]-=1
                    current.pop()
            result.sort()
            return result[0]



        """
        """
        ###dfs brute force 
        adjList=defaultdict(list)
        neededTickets=defaultdict(int)
        for source,target in tickets:
            adjList[source].append(target)
            neededTickets[(source,target)]+=1 #target

        usedTickets=defaultdict(int)
        result=[]
        current=["JFK"]

        def dfs(now,numberOfTickets):
            if numberOfTickets==len(neededTickets): #O(1)
                result.append(current.copy())
                return

            for child in adjList[now]: #remove the elemnt complelty
                if usedTickets[(now,child)]<neededTickets[(now,child)]:
                    usedTickets[(now,child)]+=1
                    current.append(child)
                    addOn=1 if usedTickets[(now,child)]==neededTickets[(now,child)] else 0
                    dfs(child,numberOfTickets+addOn)
                    current.pop()
                    usedTickets[(now,child)]-=1

        #N facotrial * N (The n part is due to having iterate over adj list same leemtn everytime, if you remove it with aset can enhacen to n facoiral )
        dfs("JFK",0)
        result.sort()

        return result[0]
        """

            

    


