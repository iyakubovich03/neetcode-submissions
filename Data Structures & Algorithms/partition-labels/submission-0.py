class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #each substring will only hold one occurence of each character
        #at the same time we want to maximize the number of substrings we generate 
        #we need to find the start index and last index for each occurence and once we hit both conditions we stop immdeitly (but must inlcude all occurences of each subtring )
        last_seen={}
        for index,value in enumerate(s):
            last_seen[value]=index

        result=[]

        left_pointer=0
        end_point=0

        for index,value in enumerate(s):
            end_point=max(end_point,last_seen[value])
            if index==end_point:
                result.append(index-left_pointer+1)
                left_pointer=index+1

        return result

        