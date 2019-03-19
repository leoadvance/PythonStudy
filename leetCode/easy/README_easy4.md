## 部分Easy题目

* [# 806. Number of Lines To Write String (numberOfLines)](https://leetcode.com/problems/number-of-lines-to-write-string/)  
题目需求数字累加后对100取余
要点：
    1. 无。

* [# 872. Leaf-Similar Trees (leafSimilar)](https://leetcode.com/problems/leaf-similar-trees/)  
题目需求对比两个二叉树最终端数据是否一致
要点：
    1. 遍历提取终端数据到list.
    2. 利用operator.eq()进行list内容一致性对比。

* [# 476. Number Complement (findComplement)](https://leetcode.com/problems/number-complement/)  
题目需求二进制正整数补码后输出。
要点：
    1. 使用bin()和int()完成2进制和10进制转换
        
* [# 893. Groups of Special-Equivalent Strings (numSpecialEquivGroups)](https://leetcode.com/problems/groups-of-special-equivalent-strings/)  
题目需求字符串按奇偶排序后判断相同字符串数量。
要点：
    1. 利用sorted()和字符串的slice特性分割字符串。
    2. 利用set()唯一性去重复。

* [# 884. Uncommon Words from Two Sentences (uncommonFromSentences)](https://leetcode.com/problems/uncommon-words-from-two-sentences/)  
题目需求判断list中不同的字符串并输出。
要点：
    1. 利用collection.Counter和split分离字符串。
    2. 利用Counter直接相加，统计输出不重复的字符串。


