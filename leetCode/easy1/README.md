## 部分Easy题目

* [Jewels and Stones (numJewelsInStones)](https://leetcode.com/problems/jewels-and-stones/)  
题目是求解两个字符串中相同字符串的个数。可以暴力求解。  
采用dict求解效率较高。dict查找key的平均消耗是O(1).  
    1. 用dict统计目标str中不同字符出现的次数,字符为key，次数为value。
    2. 遍历源str，找出dict中对应key的value相加。
 
