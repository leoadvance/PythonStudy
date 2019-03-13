## 部分Easy题目

* [# 944. Delete Columns to Make Sorted (minDeletionSize)](https://leetcode.com/problems/delete-columns-to-make-sorted/)  
题目需求是list内字符横轴轴交换后判断字符是否升序的。  
要点。
    1. 用zip进行list横纵轴交换。
    2. cpoy复制list，sort排序。

* [# 617. Merge Two Binary Trees(mergeTrees)](https://leetcode.com/problems/merge-two-binary-trees/)  
题目需求是二叉树合并
要点，学会迭代的使用和二叉树的建立。

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
