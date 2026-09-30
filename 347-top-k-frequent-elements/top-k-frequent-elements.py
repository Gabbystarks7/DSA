import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_dict = {}
        ans = []
        for num in nums:
            num_dict[num] = num_dict.get(num, 0)+1

        heap = []

        for num in num_dict:
            heapq.heappush(heap, (num_dict[num], num))

            if len(heap)>k:
                heapq.heappop(heap)

        for res in heap:
            ans.append(res[1])

        return ans

        