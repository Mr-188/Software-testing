from src.test2.rjcs import rjcs


def test_rjcs1():  # 2 10
    assert rjcs(0, 0) == 0


def test_rjcs2():  # 2 3 4 10
    assert rjcs(1, 0) == 101


def test_rjcs3():  # 2 3 6 7 9 2 10
    assert rjcs(1, 1) == 10


def test_rjcs4():  # 2 3 6 8 9 2 10
    assert rjcs(1, 2) == 20
