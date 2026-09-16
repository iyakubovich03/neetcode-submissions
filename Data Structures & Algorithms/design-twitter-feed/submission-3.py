from collections import defaultdict
import heapq
class Twitter:
    counter=0 #global counter
    def __init__(self):
        self.followers=defaultdict(set)
        self.post=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append([self.counter,userId,tweetId])
        self.counter-=1#python only suports min heap implementation

        

    def getNewsFeed(self, userId: int) -> List[int]:
        #we want the top 10 most recent from all followers
        if userId in self.followers:
            current_follower=self.followers[userId]#makes sure followers include himself
        else:
            current_follower=set()

        current_follower.add(userId)

        pointer_tracker={}#we will assign each value to length -1
        current_possible_values=[]

        #if its just one follower we will make it simple
        if len(current_follower)==1:
            #simple case j iterate over it 
            #we convert the set to a list always O(1) since 1 elent
            curr_fol=(list(current_follower))[0]      #should j be one
            print(f"this is the current follower: {curr_fol}")
            track=0
            for j in range(len(self.post[curr_fol])-1,-1,-1):
                if track==10:
                    break
                val=self.post[curr_fol][j]
                print(f"this is the current list of stuff {self.post[curr_fol]}")
                current_possible_values.append(val[2])
                track+=1
            return current_possible_values
        else:
            final_result=[]
            #this is the dagnerous case
            track=0
            for each_fol in current_follower:
                if len(self.post[each_fol])>0:
                    pointer_tracker[each_fol]=len(self.post[each_fol])-1 #set each pointer

            for key,val in pointer_tracker.items():
                heapq.heappush(current_possible_values,self.post[key][val])
                pointer_tracker[key]-=1#reduces the length

            #now we have to pop while the que not empty 
            while current_possible_values and track<10:
                curr_val=heapq.heappop(current_possible_values)#grabs the teh biggest oen 
                final_result.append(curr_val[2])#grabs tweet id
                track+=1
                #now we have to update teh que 
                if pointer_tracker[curr_val[1]]>=0: #this is future position
                    heapq.heappush(current_possible_values,self.post[curr_val[1]][pointer_tracker[curr_val[1]]])
                    pointer_tracker[curr_val[1]]-=1
                #now the array is filled up back up 

        return final_result

            #now we have a dict wiht all poinhters


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
