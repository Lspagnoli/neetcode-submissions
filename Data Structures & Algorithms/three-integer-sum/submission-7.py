class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []

        nums.sort()

        sol = []
 
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                elif curSum == 0:
                    if [nums[i], nums[l], nums[r]] not in sol:
                        sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    continue
                        

        return sol