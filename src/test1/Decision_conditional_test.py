from src.test1.rjcs import rjcs


# 判定–条件覆盖
# 使得程序中的每个判断的取真分支和取假分支至少经历一次，即判断真假值均曾被满足
def test_rjcs1():
    assert rjcs(2, 0, 4) == (2, 0, 3)  # T1 T2 T3 T4


def test_rjcs2():
    assert rjcs(1, 1, 1) == (1, 1, 1)  # F1 F2 F3 F4
