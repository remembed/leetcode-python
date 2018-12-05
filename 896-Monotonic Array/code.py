class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n=len(A)
        count1=0
        count2=0
        for i in range(0,n-1):
            temp=A[i+1]-A[i]
            if temp>=0:
                count1+=1
            if temp<=0:
                count2+=1
        if count1==n-1 or count2==n-1:
            return True
        else:
            return False
