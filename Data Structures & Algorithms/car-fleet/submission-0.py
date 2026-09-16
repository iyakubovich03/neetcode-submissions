class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        timeToFinish=[]
        for index in range(len(position)): #speed limit here
            currPosition=position[index]
            currSpeed=speed[index]
            timeToFinish.append((target-currPosition)/currSpeed)
        positionTime=list(zip(position,timeToFinish)) 
        positionTime.sort()
        result=[]
        for index in range(len(positionTime)-1,-1,-1):                               
            currentPosition,currentTime=positionTime[index]
            if result and result[-1]>=currentTime:
                #pop the previous 
                continue
            else:
                result.append(currentTime)
        return len(result)