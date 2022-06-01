class rjcs:
    pass

# 复杂度为4
def rjcs(i_count, i_flag):
    i_temp = 0                          # 1
    while i_count > 0:                  # 2
        if 0 == i_flag:                 # 3
            i_temp = i_count + 100      # 4
            break                       # 5
        else:
            if 1 == i_flag:             # 6
                i_temp = i_temp + 10    # 7
            else:
                i_temp = i_temp + 20    # 8
        i_count = i_count - 1           # 9

    return i_temp                       # 10



