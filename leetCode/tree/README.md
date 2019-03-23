## 二叉树 多叉树类题目

* [# 617. Merge Two Binary Trees(mergeTrees)](https://leetcode.com/problems/merge-two-binary-trees/)  
题目需求是二叉树合并
要点，学会迭代的使用和二叉树的建立。

* [# 965. Univalued Binary Tree(isUnivalTree)](https://leetcode.com/problems/univalued-binary-tree/)  
题目需求是二叉树遍历看是否有不同数值。

* [# 700. Search in a Binary Search Tree(searchBST)](https://leetcode.com/problems/search-in-a-binary-search-tree/)  
题目需求遍历二叉树返回指定值。  
要点：可以利用该题二叉树左边值小于右边的特性减少循环次数。


* [# 637. Average of Levels in Binary Tree(averageOfLevels)](https://leetcode.com/problems/average-of-levels-in-binary-tree/)  
题目需求返回二叉树每层平均值  
要点：
    1. 利用堆栈方式层序遍历二叉树。并求平均值


* [# 104. Maximum Depth of Binary Tree (maxDepth)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)  
题目求二叉树最大深度
要点：
    1. 利用堆栈方式层序遍历二叉树求深度。  
    
    
* [# 669. Trim a Binary Search Tree (trimBST)](https://leetcode.com/problems/trim-a-binary-search-tree/)  
题目需求，删除二叉树中指定节点。
要点：
    1. 递归解决。跳过要删除的节点，直接链接到下一层。      