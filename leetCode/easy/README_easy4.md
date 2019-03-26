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

* [# 682. Baseball Game (calPoints)](https://leetcode.com/problems/baseball-game/)  
题目需求根据一定规则对字符串相加减求和
要点：
    1. 利用int()把str转成整数。再利用sum求和。
    2. 利用list.pop()删除列表元素。

* [# 463. Island Perimeter (islandPerimeter)](https://leetcode.com/problems/island-perimeter/)  
题目需求判断二维数组内数字1相邻1的个数。
暴力遍历求解。

* [# 1020. Partition Array Into Three Parts With Equal Sum (canThreePartsEqualSum)](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)  
题目需求list内是否可以分成3组和相等的数
思路：
    1. 如果能正好分三组，每组和必然是总和三分之一。
    2. 遍历统计满足和等于三分之一的数据组数。
   

* [# 868. Binary Gap (binaryGap)](https://leetcode.com/problems/binary-gap/)  
题目需求正整数的二进制中相邻1的最大距离
要点：
    1. 注意二进制仅仅含有1个1的情况（2的n次方）
    2. 遍历判断    
    
* [# 412. Fizz Buzz (fizzBuzz)](https://leetcode.com/problems/fizz-buzz/)  
题目需求判断数据是否被3，5，15整除
要点：
    1. 注意覆盖N+1
         