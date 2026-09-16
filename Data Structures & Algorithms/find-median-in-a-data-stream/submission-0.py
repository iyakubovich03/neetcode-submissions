class MedianFinder:

    def __init__(self):
        self.track=[]
        

    def addNum(self, num: int) -> None:
        #needs to be added in O(n)
        if not self.track:
            self.track.append(num)
            return
        new_val=[]
        change=-1
        #check outter bounds to reduce one iteration
        if num<=self.track[0]:
            change=0
        elif num>=self.track[-1]:
            change=len(self.track)
        else:
            for index in range(len(self.track)):
                curr_val=self.track[index]
                if num<=curr_val:#if less htan 
                    change=index
                    break
        #now we can nromally 
        for i in range(0,change):
            cur_val=self.track[i]
            new_val.append(cur_val)
        new_val.append(num)
        for i in range(change,len(self.track)):
            cur_val=self.track[i]
            new_val.append(cur_val)
        print(new_val)
        self.track=new_val

        

    def findMedian(self) -> float:
        #either odd or even 
        if not self.track:
            return 0
        if (len(self.track)%2!=0):#means odd
            return self.track[(len(self.track)-1)//2]
        else: 
            #even you want the next correspodnign 
            val1=self.track[(len(self.track)-1)//2]
            val2=self.track[len(self.track)//2]
            return (val2+val1)/2

        