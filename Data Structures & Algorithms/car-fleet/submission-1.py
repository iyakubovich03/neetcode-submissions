class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeToFinish=[]
        for index in range(len(position)):
            currPosition=position[index]
            currSpeed=speed[index]
            timeToFinish.append((target-currPosition)/currSpeed)
        positionTime=list(zip(position,timeToFinish)) 
        positionTime.sort()
        total=1
        time=positionTime[-1][1]
        for index in range(len(positionTime)-2,-1,-1):                               
            currentPosition,currentTime=positionTime[index]
            if time>=currentTime:
                #pop the previous 
                continue
            else:
                time=currentTime
                total+=1
        return total
        #time NLOGN space N