class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(l: int, h: int) -> int:

            if h < l:
                return -1

            m = (l + h) // 2

            if nums[m] == target:
                return m
            
            elif nums[m] < target:
                return helper(m+1, h)

            elif nums[m] > target:
                return helper(l, m-1)



        return helper(0, len(nums)-1)
