#Kth Largest Element in a Stream : https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap=nums
        heapq.heapify(self.heap)
        while len(nums)>k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap,val)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
