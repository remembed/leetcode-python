This is a explanation.
1、题目要求：
判断一个数是否能被另一个整数整除
输入格式
输入包括两个由空格分开的整数 M 和 N(1\leq M,N \leq 500)N(1≤M,N≤500)。
输出格式
输出包括一行，如果 M 可以被 N 整除就输出YES，否则输出NO（结果大小写敏感）。




2、解题思路：
首先定义一个变量，用input的方法来获取数据，题目中要求两个由空格分开的整数，
所以我们要用到split来分隔两个数split（' '）引号里什么都不写说明是空格分隔。
然后用if来进行判断；注意一点：split分隔后获取的数据是一个列表，我们要把它转化为一个整数才能进行计算
% 就是数学中的除号，如果两数相除等于0说明能被整除。
最后能被整除则用print输出YES，不能的话就用esle语句，print输出NO。
