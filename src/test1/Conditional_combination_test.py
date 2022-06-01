from src.test1.rjcs import rjcs


# 条件组合覆盖
# 执行足够的例子，使得每个判定中条件的各种可能组合都至少出现一次。
def test_rjcs1():
    assert rjcs(2, 0, 4) == (2, 0, 3)  # T1 T2 T3 T4


def test_rjcs2():
    assert rjcs(2, 1, 2) == (2, 1, 3)  # T1 F2 T3 F4


def test_rjcs3():
    assert rjcs(1, 0, 4) == (1, 0, 5)  # F1 T2 F3 T4


def test_rjcs4():
    assert rjcs(1, 1, 1) == (1, 1, 1)  # F1 F2 F3 F3
