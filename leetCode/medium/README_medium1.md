## 部分Medium题目

* [# 1022. Smallest Integer Divisible by K (smallestRepunitDivByK)](https://leetcode.com/problems/smallest-integer-divisible-by-k/)  
题目是求解一个全部由1组成的数字能否被另一个数字整除。 
暴力求解。模拟除法计算过程。
 
* [# 1021. Best Sightseeing Pair (maxScoreSightseeingPair)](https://leetcode.com/problems/best-sightseeing-pair/)  
题目是求解两个list 两两相加最大值。
要点：
    1. 利用i < j特性遍历，求出起点到当前i位置i的最大值。用该值与A[j] - j求和并取和的最大值。
    
 
    