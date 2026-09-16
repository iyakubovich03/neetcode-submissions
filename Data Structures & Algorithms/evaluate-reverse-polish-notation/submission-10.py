class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #start from start 
        prev=[] #use stack to hit most recent
        for index in range(len(tokens)):
            value=tokens[index]
            if value=="+":
                most_recent=prev.pop()
                bf=prev.pop()
                prev.append(bf+most_recent)
            elif value=="*":
                most_recent=prev.pop()
                bf=prev.pop()
                prev.append(bf*most_recent)
            elif value=="-":
                most_recent=prev.pop()
                bf=prev.pop()
                prev.append(bf-most_recent)
            elif value=="/":
                most_recent=prev.pop()
                bf=prev.pop()
                prev.append(int((bf/most_recent)))
            else:
                prev.append(int(value))
  
        return prev[-1]
       

