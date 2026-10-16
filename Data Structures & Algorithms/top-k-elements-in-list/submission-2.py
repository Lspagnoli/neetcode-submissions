class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        vals = []

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] +=1

        temp = []
        for item in d:
            temp.append([d[item], item])
        
        temp = sorted(temp, reverse=True)

        for i in range(k):
            vals.append(temp[i][1])
            

        return vals