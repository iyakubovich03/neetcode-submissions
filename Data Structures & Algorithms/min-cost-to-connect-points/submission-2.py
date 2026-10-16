class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # manhattan distance [xi-xj]+[yi-yj]
        #brute force consider all paths from the each point,(calualte manhanntten distnace for each and choose the smallest one, we can connect it and pop off the previous point)(each edge used at most once)
        #
        reference={}
        size={}
        for point in points:
            reference[tuple(point)]=tuple(point)
            size[tuple(point)]=1

        def find(cord):
            if reference[cord]==cord:
                return cord
            reference[cord]=find(reference[cord])
            return reference[cord]

        def union(cord1,cord2):
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
            for index2 in range(index+1,len(points)):
                xi,yi=points[index]
                xj,yj=points[index2]
                dist=abs(xi-xj)+abs(yi-yj)
                heapq.heappush(heap,(dist,(xi,yi),(xj,yj)))
        edges=len(points)-1
        minCost=0

        while heap:
            dist,cord1,cord2=heapq.heappop(heap)
            if find(cord1)==find(cord2):
                continue
            edges-=1
            minCost+=dist
            if edges==0:
                return minCost
            union(cord1,cord2)
            
        return 0

