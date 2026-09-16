from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        #need to track the tweets#we pop offf the 10 most recent 
        #need to track the user that each person follows
        self.tweets=[]
        self.follows=defaultdict(set)#this tracks the people they follow
        #view 10 most recent feeds 
        #can this be optimized

    def postTweet(self, userId: int, tweetId: int) -> None:
        #we arent popping
        self.tweets.append([userId,tweetId])#adding the feed 
        #this seems O(n)#can this be optimized via binary heap O(log(n))
        # i have an array and i need to return the 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        possible_followers=self.follows[userId]#set of followers
        possible_followers.add(userId)
        feed=[]
        if not self.tweets:
            return None
        gren=len(self.tweets)-1
        print(gren)
        print(self.tweets)
        while gren>=0 and len(feed)<10:
            print(f"the current gren is {gren}")
            user_id,tweet_id=self.tweets[gren]
            if user_id in possible_followers:
                feed.append(tweet_id)
            gren-=1
        return feed
        #need to return top 10 feeds of themselves n the people they follow
        #if not 10 just return how many there are 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)#this adds to the set of their follows
        
        #need to track this somehow 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)#this adds to the set of their follows
        
