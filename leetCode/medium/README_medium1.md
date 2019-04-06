## 部分Medium题目

* [# 1022. Smallest Integer Divisible by K (smallestRepunitDivByK)](https://leetcode.com/problems/smallest-integer-divisible-by-k/)  
题目是求解一个全部由1组成的数字能否被另一个数字整除。 
暴力求解。模拟除法计算过程。
 
* [# 1021. Best Sightseeing Pair (maxScoreSightseeingPair)](https://leetcode.com/problems/best-sightseeing-pair/)  
题目是求解两个list 两两相加最大值。
要点：
    1. 利用i < j特性遍历，求出起点到当前i位置i的最大值。用该值与A[j] - j求和并取和的最大值。
    
* [# 1017. Convert to Base -2 (baseNeg2)](https://leetcode.com/problems/convert-to-base-2/)  
题目是求十进制数转换成基于-2的二进制数。  
要点：
    1. 利用2 = 4 + (-2), 8 = 16 + (-8), _2^(n - 1) = (-2)^n + (-2)^(n-1)_.求解，N为偶数。

* [807. Max Increase to Keep City Skyline (maxIncreaseKeepingSkyline)](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)  
题目求二维list里每个位置所处行列最大值中较小的数。   
要点：无，遍历求解。
 

* [950. Reveal Cards In Increasing Order (deckRevealedIncreasing)](https://leetcode.com/problems/reveal-cards-in-increasing-order/)  
题目目的，按要求变换list数字顺序。    
要点：
    1. 利用colletions.deque()减少pop和左侧插入数据时间。
 
 
* [973. K Closest Points to Origin (kClosest)](https://leetcode.com/problems/k-closest-points-to-origin/)  
题目目的，求二维list内每个数据平方和并排序。    
要点：
    1. 利用sort 按关键字key排序。
    2. 利用lambda遍历数组计算平方和。
    
* [921. Minimum Add to Make Parentheses Valid (minAddToMakeValid)](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)  
题目目的，判断不成对的括号数量。    
要点：
    1. 出现左括号加一，右括号减一。
    2. 如果有额外的又括号，不能直接减一，额外记录并计入总数。                    