class MinStack:

    def __init__(self):
        self.array=[]
        self.minArray=[]

    def push(self, val: int) -> None:
        self.array.append(val)
        self.minArray.append(min(val,self.minArray[-1] if self.minArray else float('inf')))

        

    def pop(self) -> None:
        self.array.pop()
        self.minArray.pop()
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.minArray[-1]
        
