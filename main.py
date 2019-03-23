# coding=utf-8

from varStudy import *

# 相对路径导入私有库
import leetCode.easy.easy1
import leetCode.easy.easy2
import leetCode.easy.easy3
import leetCode.easy.easy4
import leetCode.tree.tree as leetCodeTree
import pyGame.snake.snake as snakeGame

if __name__ == "__main__":
    print("python study!")

    # varStudy = VariableClass()
    # varStudy.run()
    leetCodeTree = leetCodeTree.Solution()
    leetCodeTree.run()
    leetCode = leetCode.easy.easy4.SolutionEasy()
    # leetCode.run()
    pygameSnkae =snakeGame.snake("pyGameSnake")
    # pygameSnkae.run()
