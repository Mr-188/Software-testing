from src.test1.rjcs import rjcs


# 判定覆盖
# 使得程序中的每一个判断的取真分支和取假分支至少经历一次，即判断真假值均曾被满足
def test_rjcs1():
    assert rjcs(2, 0, 4) == (2, 0, 3)
def test_rjcs2():
    assert rjcs(1, 1, 1) == (1, 1, 1)