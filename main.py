# coding=utf-8

from varStudy import *

# 相对路径导入私有库
import leetCode.easy.easy1
import leetCode.easy.easy2 as leetCodeEasy2
import leetCode.easy.easy3 as leetCodeEasy3
import leetCode.easy.easy4 as leetCodeEasy4
import leetCode.easy.easy5 as leetCodeEasy5
import leetCode.medium.medium1 as leetCodeMedium
import leetCode.tree.tree as leetCodeTree
import pyGame.snake.snake as snakeGame

if __name__ == "__main__":
    print("python study!")

    # varStudy = VariableClass()
    # varStudy.run()

    # leetCodeTree = leetCodeTree.Solution()
    # leetCodeTree.run()

    # leetCode = leetCodeEasy2.SolutionEasy()
    # leetCode.run()

    # leetCode = leetCodeEasy3.SolutionEasy()
    # leetCode.run()

    leetCode = leetCodeEasy5.SolutionEasy()
    leetCode.run()

    # leetCodeMedium = leetCodeMedium.SolutionMedium()
    # leetCodeMedium.run()

    # pygameSnkae =snakeGame.snake("pyGameSnake")
    # pygameSnkae.run()
