一、题目描述：
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：
输入：[1,2,2,3]
输出：true

示例 2：
输入：[1,3,2]
输出：false

示例 3：
输入：[1,1,1]
输出：true

二、解题思路 
判断是否单调直接判断该数组是否有序即可，设置一个计数器，用来存储符合条件的数的数量，初始值为 1；
第一次遍历数组，如果后一元素小于等于前一元素则计数器加1，不相等则直接下一次循环，遍历完成后判断计数器值是否等于数组的长度，是则直接返回true；
否则将计数器值置为1，重新遍历记载数组是否单调递增，原理同单调递减；如果既不是递增也不是递减，则返回false。
