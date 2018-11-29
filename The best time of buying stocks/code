class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #prices是一个列表，先测量它的长度
        if len(prices)<2:
            return 0
        #定义一个最小价格，0是下标，意思就是列表中第一个数
        min_price = prices[0]
        #定义一个最大利润，假设最开始为0
        max_profile = 0
        #遍历一下这个列表
        for i in prices:
        #min是一个比较函数，比较两个或以上的数值的大小；max同理
            min_price = min(min_price, i)
            max_profile = max(max_profile, i - min_price)
        return max_profile
