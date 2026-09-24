from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.following=defaultdict(set) #folowerId: foloweee1,folowee2
        self.tweets=defaultdict(list) #userId: [(time,tweetId),...]
        self.time=0
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #10logk (we do this 10 times)
        heap=[]
        result=[] #at most 10

        following=self.following[userId]
        following.add(userId)
        for followee in following:
            currentTweets=self.tweets[followee]
            if currentTweets:
                heapq.heappush(heap,[-currentTweets[-1][0],len(currentTweets)-1,currentTweets]) #max time (negative since min heap) (time,tweetId,index,reference)
        for _ in range(10):
            if not heap: 
                break
            _,index,ref=heapq.heappop(heap)
            currentTweetId=ref[index][1]
            result.append(currentTweetId)
            if index-1>=0:
                #readd it
                time,_=ref[index-1]
                heapq.heappush(heap,[-time,index-1,ref])

        return result


        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
