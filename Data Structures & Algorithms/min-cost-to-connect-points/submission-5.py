class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # manhattan distance [xi-xj]+[yi-yj]
        #brute force consider all paths from the each point,(calualte manhanntten distnace for each and choose the smallest one, we can connect it and pop off the previous point)(each edge used at most once)
        #
        
        # Prims Algo 

        unvisited=set()
        for a,b in points:
            unvisited.add((a,b)) #need to remove the first one 
        
        #(distance,new cordinate)
        heap=[]
        heapq.heappush(heap,(0,tuple(points[0])))# initalize with random
        minCost=0
        edges=len(unvisited) #number of iterations

        while heap:
            dist,current=heapq.heappop(heap)
            if current not in unvisited:
                continue
            #grab all the neighbors 
            unvisited.remove(current)
            minCost+=dist
            edges-=1
            if edges==0:
                return minCost

            for a,b in unvisited:
                a2,b2=current
                dist=abs(a2-a)+abs(b2-b)
                heapq.heappush(heap,(dist,(a,b)))
        
        


        """
        Kruskals Algo

        reference={} # O(N)
        size={}
        for point in points:
            reference[tuple(point)]=tuple(point)
            size[tuple(point)]=1

        def find(cord): #O(1)
            if reference[cord]==cord:
                return cord
            reference[cord]=find(reference[cord])
            return reference[cord]

        def union(cord1,cord2): #O(1)
            parent1=find(cord1)
            parent2=find(cord2)
            if parent1==parent2:
                return False
            if size[parent1]<size[parent2]:
                parent1,parent2=parent2,parent1

            reference[parent2]=parent1
            size[parent1]+=size[parent2]

        heap=[]
        for index in range(len(points)-1):
            for index2 in range(index+1,len(points)): #O(N^2)
                xi,yi=points[index]
                xj,yj=points[index2]
                dist=abs(xi-xj)+abs(yi-yj)
                heapq.heappush(heap,(dist,(xi,yi),(xj,yj))) #logn-> n^2 log n^2
        edges=len(points)-1
        minCost=0

        while heap: #n^2 log n^2
            dist,cord1,cord2=heapq.heappop(heap)
            if find(cord1)==find(cord2):
                continue
            edges-=1
            minCost+=dist
            if edges==0:
                return minCost
            union(cord1,cord2)

        return 0
        """
        # n-1, n-2,n-3...0. (n-1)+(n-2)+...=*n + - =N

