## 部分Easy题目

* [# 976. Largest Perimeter Triangle (largestPerimeter)](https://leetcode.com/problems/largest-perimeter-triangle/)  
题目需求判断list内数据能否构成三角形，并返回最大周长。  
要点：
    1. 要求最大周长，先对数组进行降序排列并遍历。
    2. 通过两边之和大于第三边来判断三角形。 


* [# 1029. Binary Prefix Divisible By 5 (prefixesDivBy5)](https://leetcode.com/problems/binary-prefix-divisible-by-5/)  
题目需求一个数据是否能被5整除。   
要点：
    1. 利用除法特性，直接用余数迭代。

* [# 888. Fair Candy Swap (fairCandySwap)](https://leetcode.com/problems/fair-candy-swap/)  
题目需求交换两个列表中的某个数字，使两个列表数字和相等。     
要点：
    1. 判断数组里是否包含某数据时先把list转换为set().
    2. 先求两数组和的差值的一半。遍历数组A，找到数据+差值=B数组中数据的数。
    
* [# 521. Longest Uncommon Subsequence I (findLUSlength)](https://leetcode.com/problems/longest-uncommon-subsequence-i/)  
特别无聊的题目，不知道出题人想考什么。

* [# 5016. Remove Outermost Parentheses (removeOuterParentheses)](https://leetcode.com/problems/remove-outermost-parentheses/)  
题目要求，清除字符串最外层括号，并输出剩余内容。  
要点：
    1. 无
    
* [# 917. Reverse Only Letters (reverseOnlyLetters)](https://leetcode.com/problems/reverse-only-letters/)  
题目要求，对字符串内字母前后顺序交换，非字母保持不变。  
要点：
    1. str转成list进行处理。最终list再转str。
 
* [# 860. Lemonade Change (lemonadeChange)](https://leetcode.com/problems/lemonade-change/)  
题目要求判断能否准确找零  
要点：
    1. 分别设置两个变量记录当前5元和10元数量。以此判断能否找零。  