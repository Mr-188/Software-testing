from src.test1.rjcs import rjcs


# 路径覆盖
# 覆盖程序中的所有可能执行的路径
def test_rjcs1():
    assert rjcs(1, 1, 1) == (1, 1, 1)  # 1 3 5


def test_rjcs2():
    assert rjcs(3, 0, 3) == (3, 0, 1)  # 1 2 3 5


def test_rjcs3():
    assert rjcs(1, 2, 4) == (1, 2, 5)  # 1 3 4 5


def test_rjcs4():
    assert rjcs(2, 0, 4) == (2, 0, 3)  # 1 2 3 4 5
