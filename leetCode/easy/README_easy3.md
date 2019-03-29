## 部分Easy题目


* [# 883. Projection Area of 3D Shapes (projectionArea)](https://leetcode.com/problems/projection-area-of-3d-shapes/)  
题目比较唬人，引入一堆干扰问题，真实需求是三点，1.求list内部非零元素个数。2. 求每组数据最大值。3. 横纵坐标变换后再求一次。
要点：
    1. 利用zip(*x)完成矩阵变换。
    
* [# 559. Maximum Depth of N-ary Tree (maxDepth)](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)  
题目求多叉树最大深度。迭代求解。
要点：
    1. 通过关键字nonlocal可以使用外层变量。
    
* [# 908. Smallest Range I (smallestRangeI)](https://leetcode.com/problems/smallest-range-i/)  
题目求list内最大值和最小值差值。引入参数k作为调节量。
要点：
    1. 使用max，min求最大最小值或者用sort对数组排序。    
    
    
    
* [# _811. Subdomain Visit Count_ (subdomainVisits)](https://leetcode.com/problems/subdomain-visit-count/)  
题目求字符串分割，并统计相同字符数量。
要点：
    1. 利用split分割字符串。
    2. 利用dict记录不同字符串出现次数。
    
* [# _867. Transpose Matrix (transpose)](https://leetcode.com/problems/transpose-matrix/)  
题目需求list矩阵转换
要点：
    1. 利用map，zip完成矩阵转换
  
* [# _876. Middle of the Linked List (middleNode)](https://leetcode.com/problems/middle-of-the-linked-list/)  
题目需求后半部分listnode
要点：
    1. 利用快慢指针。快指针移动是慢指针两倍。
    
  
* [# _344. Reverse String (reverseString)](https://leetcode.com/problems/reverse-string/)  
题目需求list逆序显示
要点：
    1. 利用list[::-1].
    
* [# _821. Shortest Distance to a Character (shortestToChar)](https://leetcode.com/problems/shortest-distance-to-a-character/)  
题目核心求特定字符在字符串位置。

* [# _762. Prime Number of Set Bits in Binary Representation (countPrimeSetBits)](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)  
题目求给定区间内数字的二进制下1的位数是素数个数。  
要点：
    1. 数据不会大于1百万，即24bit，所以穷举出24内素数个数做字典。
    2. 利用bin转换十进制为二进制。
    3. 利用count数出1的个数并和字典比对。
    4. 字典可以只有key，没有value。
    
* [# _693. Binary Number with Alternating Bits (hasAlternatingBits)](https://leetcode.com/problems/binary-number-with-alternating-bits/)  
题目求给某整数的二进制数下是否有连续的0或者1.  
方法：利用bin求出二进制后遍历。    