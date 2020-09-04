#LeetCode link - https://leetcode.com/problems/partition-labels/
#Uses greedy approach
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = dict()
        for i in range(0,len(S)):
            last_index[S[i]] = i
    
        output_list = []
        count = 0
        max_range = 0
        for i in range(0,len(S)):
            if(i>max_range):
                max_range = last_index[S[i]]
                output_list.append(count)
                count = 0
            if(last_index[S[i]]>max_range):
                max_range = last_index[S[i]]
            count+=1
            
         
        output_list.append(count)
        return output_list