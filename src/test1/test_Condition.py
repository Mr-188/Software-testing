from src.test1.rjcs import rjcs


# 条件覆盖
# 使每个判断中的每个条件的可能取值至少满足一次
def test_rjcs1():
    assert rjcs(2, 0, 4) == (2, 0, 3)


def test_rjcs2():
    assert rjcs(1, 1, 1) == (1, 1, 1)
