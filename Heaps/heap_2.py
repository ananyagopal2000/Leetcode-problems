# K Closest Points to Origin : https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n=len(points)
        heap=[]
        res=[]
        heapq.heapify(heap)

        for point in points:
            distance=sqrt(pow(point[0],2)+pow(point[1],2))
            heapq.heappush(heap,(distance,point))

        while len(heap)>n-k:
            dist, point=heappop(heap)
            res.append(point)
        return res
