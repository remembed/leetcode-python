class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A)-1
        while letf < right:
            mid = (left + right)//2
            if A[mid] < A[mid+1]:
                left = mid +1
            if A[mid] < A[mid+1]
                right = mid
        else:
            return left
