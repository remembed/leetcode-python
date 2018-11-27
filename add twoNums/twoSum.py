#方法一：
class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 用len()方法取得nums列表的长度
        n = len(nums)
        #x取值从0到n但是不包括n
        for x in range(n):
        # y取值从x+1一直到n（不包括n）
        # 用x+1是减少不必要的循环,y的取值肯定是比x大
            for y in range(x+1,n):
        # 假如 target-nums[x]的某个值存在于nums中
                if nums[y] == traget - nums[x]:
                    # 返回x和y
                    return x, y
                    break
                else:
                    continue
#方法二：
class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #用len()方法取得nums列表长度
        n = len(nums)
        #x从0到n取值（不包括n）
        for x in range(n):
            a = target - nums[x]
            #用in关键字查询nums列表中是否有a
            if a in nums:
                #用index函数取得a的值在nums列表中的索引
                y = nums.index(a)
                #假如x=y,那么就跳过,否则返回x,y
                if x == y:
                    continue
                else:
                    return x,y
                    break
            else :
                continue
#方法三:
class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #用len()方法取得nums列表长度
        n = len(nums)
        #创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            #字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]],x
            #否则往字典增加键/值对
            else:
                d[a] = x
        #边往字典增加键/值对，边与nums[x]进行对比
