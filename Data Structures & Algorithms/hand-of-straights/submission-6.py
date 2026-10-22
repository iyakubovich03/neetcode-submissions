from collections import deque, defaultdict
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        quick check on divisibility
        we know the number of groups hand/groupsize -> we will store the state (previous,ocurrence)
        we are pop off the smallest value and add it to the first state where !=previous and diff is one and size is less than groupSize
        if we can populate all the groups then its valid 
        """
        if len(hand)%groupSize:
            return False

        frequency=defaultdict(int)
        for value in hand:
            frequency[value]+=1

        heap=[]

        for key,value in frequency.items():
            heapq.heappush(heap,(key,value))

        cannot_be_used=[]

        previous=None
        group_size=0

        while heap:
            current_element,freq=heapq.heappop(heap)
           

            if previous is not None and current_element-previous!=1:
                print
                return False

            previous=current_element
            group_size+=1
            
            if freq-1>0:
                cannot_be_used.append((current_element,freq-1))

            if group_size==groupSize:
                #append back all other elements 
                for v in cannot_be_used:
                    heapq.heappush(heap,v)
                cannot_be_used=[]
                previous=None
                group_size=0

        return group_size==0
        #basically pop and push each elment it occurs, so roughly N times, so NlogN

        """
        if len(hand)%groupSize: #not divisible
            return False

        number_of_groups=int(len(hand)/groupSize)

        deq=deque()

        for _ in range(number_of_groups):
            deq.append([None,0])

        heapq.heapify(hand)
        while hand:
            
            smallest_element=heapq.heappop(hand)
            #we want to assign the elemnt 

            pointer=0
            while pointer<len(deq):
                #we check if 
                prev,count=deq[pointer]
                if prev!=smallest_element:
                    if prev is not None and abs(smallest_element-prev)!=1:
                        return False
                    #otherwise we can update 
                    deq[pointer][0],deq[pointer][1]=smallest_element,deq[pointer][1]+1
                    if deq[pointer][1]==groupSize:
                        deq.popleft()

                    break #get out of the loop

                pointer+=1

            if pointer>0 and pointer==len(deq): #this breaks in the case where its 0
                return False
        return len(deq)==0

        """
        # if there were no reepated values we can simply use a heap track previous and group size, if we reach a state that differnce sint one then return false, when we reach group size reset both and do this to the end return false, or you can srot and bascilly just iterate in batcehs for four 
        #or sort and itearte till end and bascilly skip indexes that are divisbl eby group size, otherwise if prevous state sint equal to prev+1 then return false

        #the whole optimization part here is the duplicated states (as that causes us to geenrate anotehr group) in a chopped way, it would be better if we can bascilly iterate for groupSize()* groups (removing elments that we use if valid, and if duplciate remove from a diciontary once reaches 0 then we can remove it, otherwise we skip over n then remove )


#basiclly put frequency and the value in a heap, track current group, we pop if size is now 0 remove, otherwise 
#put it on a quue still we finish teh group
#if diff is greater than 1 then false


            


        
        