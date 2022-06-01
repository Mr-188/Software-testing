from src.test1.rjcs import rjcs


# 语句覆盖
# 使程序中的每个可执行语句至少执行一次。
def test_rjcs1():
    assert rjcs(2, 0, 4) == (2, 0, 3)
