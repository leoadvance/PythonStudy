## 部分Easy题目

* [# 944. Delete Columns to Make Sorted (minDeletionSize)](https://leetcode.com/problems/delete-columns-to-make-sorted/)  
题目需求是list内字符横轴轴交换后判断字符是否升序的。  
要点。
    1. 用zip进行list横纵轴交换。
    2. cpoy复制list，sort排序。


* [# 852. Peak Index in a Mountain Array(peakIndexInMountainArray)](https://leetcode.com/problems/peak-index-in-a-mountain-array/)  
题目本质是求解list数组最大值出现的位置。（陷进，list内不仅可以装int型，也能装float型）。  
要点：
    1. 利用max函数求list最大值。
    2. 利用list.index得出最大值出现的位置。
    
* [# 933. Number of Recent Calls(ping)](https://leetcode.com/problems/number-of-recent-calls/)  
题目本质是掌握list的appen和pop使用。更高效的做法是使用collections.deque()的popleft来代替list的pop操作。 

* [# 1002. Find Common Characters(commonChars)](https://leetcode.com/problems/find-common-characters/)  
题目本质是输出list内每个str中都出现的相同字符。  
要点:
    1. 学习用collections.Counter函数统计str中出现每个字符串的数量。并转换成dict。
    2. 遍历list，用min求取相同数量字符最小值。
    3. 用extend添加到list中。 了解extend和append的区别。

* [# 985. Sum of Even Numbers After Queries(sumEvenAfterQueries)](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)  
题目要求输入list的数据和原list相加，并返回偶数的和。  
要点:
    1. 不能直接暴力遍历，效率过低。
    2. 先算出原始list偶数和，后续每次只对增量做操作。 


* [# 922. Sort Array By Parity II(sortArrayByParityII)](https://leetcode.com/problems/sort-array-by-parity-ii/)  
题目需求list奇偶排序没有特别的。（学到了可以直接[0] * len(x)创建list）  


* [# 509. Fibonacci Number(fib)](https://leetcode.com/problems/fibonacci-number/)  
题目是典型斐波那契数列求值。  
要点：
    1. 学习a, b = c ,d使用。
    2. 注意fib(0)时返回值。
    
* [# 937. Reorder Log Files (reorderLogFiles)](https://leetcode.com/problems/reorder-log-files/)  
题目需求，按要求对list内部字符串排序  
要点：
    1. 利用split(" ", 1)把字符串分成两份。
    2. 利用sorted和key对字符串排序。
    
* [# 496. Next Greater Element I (nextGreaterElement)](https://leetcode.com/problems/next-greater-element-i/)  
题目求Alist在Blist里每个右边出现的第一个比自身大的数 
要点：
    1. 注意规避传入list为空的情况。
    2. 利用dict查询速度快以及key的唯一性。    