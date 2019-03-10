## 部分Easy题目

* [# 771. Jewels and Stones (numJewelsInStones)](https://leetcode.com/problems/jewels-and-stones/)  
题目是求解两个字符串中相同字符串的个数。可以暴力求解。  
采用dict求解效率较高。dict查找key的平均消耗是O(1).  
    1. 用dict统计目标str中不同字符出现的次数,字符为key，次数为value。
    2. 遍历源str，找出dict中对应key的value相加。
 
* [# 709. To Lower Case (toLowerCase)](https://leetcode.com/problems/to-lower-case/)  
题目是把输入字符串中大写字母（注意，只能是字母，&%这些特殊符号不算）转化成小写并返回。  
两种做法： 
    1. 建立26个字母的dict，大写字母为key，对应的小写字母为value。遍历字符串，匹配key，并用value里小写字符替换。
    2. 在ascii表里大写字符=对应小写字符-32.所以遍历字符串，发现有大写字符通过ord转成数字+32，再通过chr还原回字符格式。（这里C语言比较有优势，不用转换，直接char型相加减）    
*按直觉，方案二要经过两次字符转换并且做加法，应该比dict对比key取值要慢。实际我做测试进行2千万个数据（大小写各一半）转换，方法1比方法2快10%，但是LeetCode的测评确是方案2时间得分更高。*    
    
* [# 929. Unique Email Addresses (numUniqueEmails)](https://leetcode.com/problems/unique-email-addresses/)  
题目要求分段落删除特定字符，并且判断字符串唯一性。  
思路： 
    1. 利用split和replace功能分别分段和删除特定字符。
    2. 利用set()元素不重复特性统计不同字符串个数。（也可以用dict实现）
    
 
    
* [# 804. Unique Morse Code Words (uniqueMorseRepresentations)](https://leetcode.com/problems/unique-morse-code-words/)  
题目核心依然是字符串替换，并且判断字符串唯一性。  
思路： 
    1. 利用dict完成字符替换。
    2. 利用set()元素不重复特性统计不同字符串个数。
    
    
        
* [# 961. N-Repeated Element in Size 2N Array (repeatedNTimes)](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)  
题目核心判断list里重复出现的字符
思路： 
    1. 遍历list，并存入dict，遇到重复key停止。

        
* [# 977. Squares of a Sorted Array (sortedSquares)](https://leetcode.com/problems/squares-of-a-sorted-array/)  
题目核心乘法以及排序 学习利用<font color=blue>*sort*</font>排序
 
 
 
        
* [# 905. Sort Array By Parity (sortedSquares)](sortArrayByParity)  
题目需求按奇偶排序。  
重点：  
    1. list的append是O(1)时间复杂度的。
    2. 两个list可以直接用"+"号连接成一个。