# Main easier answer
#class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         res = []
#         for i in range(n-k+1):
#             res.append(max(nums[i:i+k]))
#         return res
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res.append(-heap[0][0])

        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))

            # Remove elements outside the current window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            res.append(-heap[0][0])

        return res

        