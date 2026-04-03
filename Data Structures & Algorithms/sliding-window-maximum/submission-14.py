class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        result = []
        count = defaultdict(int)
        l = 0

        for r, x in enumerate(nums):
            count[x] += 1
            heapq.heappush(maxheap, -x)

            if len(maxheap) > k:
                count[nums[l]] -= 1
                if nums[l] == -maxheap[0]:
                    heapq.heappop(maxheap)
                # if carrying an extra number that shouldn't exist, pop it
                if maxheap and count[-maxheap[0]] == 0:
                    heapq.heappop(maxheap)
                l += 1
            if r - l + 1 == k:
                result.append(-maxheap[0])
        
        return result