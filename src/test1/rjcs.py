# 测试


class rjcs:
    pass


def rjcs(a, b, x):
    """
    判断条件1:
            a > 1 : T1
            a <= 1 : F1
            b == 0 : T2
            b != 0 : F2
    """
    # 1
    if a > 1 and b == 0:
        # 2
        x = x / a
    """ 
    判断条件2:
            a == 2 : T3 
            a != 2 : F3
            x > 1 : T4
            x <= 1 : F4
    """
    # 3
    if a == 2 or x > 1:
        # 4
        x = x + 1
    # 5

    return a, b, x
