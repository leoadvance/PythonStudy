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
     
     
* [# 429. N-ary Tree Level Order Traversal (levelOrder)](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)  
题目需求层序遍历多叉树并输出
要点：
    1. 堆栈遍历。
    2. list.append([xxx])可以用于扩展多维list         
    

* [# 590. N-ary Tree Postorder Traversal (postorder)](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)  
题目需求多叉树遍历  
要点：
    1. 无。

* [# 589. N-ary Tree Preorder Traversal (preorder)](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)  
题目需求逆序多叉树遍历  
要点：
    1. 无。

* [# 226. Invert Binary Tree (invertTree)](https://leetcode.com/problems/invert-binary-tree/)  
题目需求二叉树翻转。  
要点：
    1. 利用堆栈层序遍历+左右分支交互。
    2. 利用迭代也能解决，但堆栈更通用。
    
* [# 559. Maximum Depth of N-ary Tree (maxDepth)](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)  
题目求多叉树最大深度。迭代求解。
要点：
    1. 通过关键字nonlocal可以使用外层变量。 
    
* [# 1022. Sum of Root To Leaf Binary Numbers (sumRootToLeaf)](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)  
题目求二叉树每条分支（二进制形式）的和。  
要点：
    1. 利用堆栈进行程序遍历。
    2. 当前节点（和）数据入栈，传递到下一层。         