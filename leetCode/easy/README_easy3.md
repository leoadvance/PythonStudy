## 部分Easy题目

* [# 590. N-ary Tree Postorder Traversal (postorder)](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)  
题目需求多叉树遍历  
要点：
    1. 无。

* [# 589. N-ary Tree Preorder Traversal (preorder)](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)  
题目需求逆序多叉树遍历  
要点：
    1. 无。


* [# 883. Projection Area of 3D Shapes (projectionArea)](https://leetcode.com/problems/projection-area-of-3d-shapes/)  
题目比较唬人，引入一堆干扰问题，真实需求是三点，1.求list内部非零元素个数。2. 求每组数据最大值。3. 横纵坐标变换后再求一次。
要点：
    1. 利用zip(*x)完成矩阵变换。
    
* [# 559. Maximum Depth of N-ary Tree (maxDepth)](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)  
题目求多叉树最大深度。迭代求解。
要点：
    1. 通过关键字nonlocal可以使用外层变量。