class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        # Brute force will find all 1 and 2 indices and find the min diff
        allOnes = []
        allTwos = []
        final = []

        for i in range(len(nums)): 
            if nums[i] == 1:
                allOnes.append(i)
            if nums[i] == 2:
                allTwos.append(i)
        
        for n in allOnes:
            for m in allTwos:
                final.append(abs(n-m))

        if not final:
            return -1
        
        
        return min(final)







        #Optimal Solution with a single pass
        # lastOne = -1
        # lastTwo = -1
        # ans = float('inf')

        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         lastOne = i
        #         if lastTwo != -1:
        #             ans = min(ans, i-lastTwo)
        #     if nums[i] == 2:
        #         lastTwo = i
        #         if lastOne != -1:
        #             ans = min(ans, i-lastOne)
        # return ans if ans!=float('inf') else -1
        
        

        