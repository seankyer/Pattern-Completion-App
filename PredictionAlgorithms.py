from scipy import stats


# Takes in a sequence of numbers and returns the next n predicted elements
def lin_reg_nums(inp_list, n):
    out = []
    for i in range(len(inp_list)):
        inp_list[i] = int(inp_list[i])
    sz = len(inp_list)
    xs = range(sz)
    res = stats.linregress(xs, inp_list)
    for x in range(n):
        out.append(int(res.intercept + res.slope * (sz + x)))
    return out


# Takes in a sequence of letters and returns the next n predicted elements
# Adjusts for upper/lowercase using offset
def lin_reg_letters(inp_list, offset, n):
    out = []
    sz = len(inp_list)
    xs = range(sz)
    for pos in range(len(inp_list)):
        inp_list[pos] = to_base26(inp_list[pos], offset)
    res = stats.linregress(xs, inp_list)
    for x in range(n):
        out.append(letters_from_base26(int(res.intercept + res.slope * (sz + x)), offset))
    return out


# Used for converting letters to an adjusted ASCII value
def to_base26(letter, offset):
    return ord(letter) - offset


# Used to process letters from adj ASCII to Characters
def letters_from_base26(val, offset):
    out = ""
    last_ele = False
    while not last_ele:
        out = chr(val % 26 + offset) + out
        last_ele = val <= 26
        val = int((val - (val % 26)) / 26)
    return out