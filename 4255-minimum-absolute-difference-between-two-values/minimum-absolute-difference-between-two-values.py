class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        lastOne = -1
        lastTwo = -1
        ans = float('inf')

        for i in range(len(nums)):
            if nums[i] == 1:
                lastOne = i
                if lastTwo != -1:
                    ans = min(ans, i-lastTwo)
            if nums[i] == 2:
                lastTwo = i
                if lastOne != -1:
                    ans = min(ans, i-lastOne)
        return ans if ans!=float('inf') else -1
        
        

        