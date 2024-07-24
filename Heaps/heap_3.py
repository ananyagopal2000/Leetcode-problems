# Top K Frequent Elements : https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        n=len(nums)
        heap=[]
        heapq.heapify(heap)
        count_num={}
        res=[]

        for number in nums:
            if number not in count_num:
                count_num[number]=1
            else:
                count_num[number]+=1

        for num,count in count_num.items():
            heapq.heappush(heap,(count,num))

        while len(heap)>k:
            heapq.heappop(heap)

        for count,num in heap:
            res.append(num)

        return res
