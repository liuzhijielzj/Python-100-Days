"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools
for permutation in itertools.permutations('ABCD'):
    print(permutation)
itertools.combinations('ABCDE', 3)
itertools.product('ABCD', '123')