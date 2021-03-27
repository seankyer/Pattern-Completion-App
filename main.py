from scipy import stats
import re

# Python program to take in a pattern
# and return a prediction of the next n elements


# Prompts the user to input a sequence of data and terminates on 'exit'
def get_user_pattern():
    inp_list = []
    latest_input = ''
    while latest_input != 'exit':
        if latest_input != '':
            inp_list.append(latest_input)
        latest_input = input("Please enter your pattern element:\n")
    return inp_list


# Breaks input string into a list by each data type that constitutes
# the overall word
def parse_pattern(s_t, p):
    pattern_arr = []
    for m in range(len(p)):
        for n in range(len(s_t)):
            if m == 0:
                pattern_arr.append([s_t[n]])
            if s_t[n] == "C":
                mat = re.search('^[A-Z]', p[m])
                pattern_arr[n].append(mat.group(0))
                p[m] = re.sub(r'^[A-Z]', "", p[m], 1)
            elif s_t[n] == "L":
                mat = re.search('^[a-z]', p[m])
                pattern_arr[n].append(mat.group(0))
                p[m] = re.sub(r'^[a-z]', "", p[m], 1)
            elif s_t[n] == "N":
                mat = re.search('^[0-9]+', p[m])
                pattern_arr[n].append(mat.group(0))
                p[m] = re.sub(r'^[0-9]+', "", p[m], 1)
    return pattern_arr


# Generates predictions on parsed data and manages
# direction of sequences to appropriate lin-reg methods
def generate_predictions(p, n):
    out = []
    for i in range(n):
        out.append("")
    for ele in p:
        seq_list = ele[1:]
        if ele[0] == "C":
            list_concat(out, lin_reg_letters(seq_list, 65, n))
        elif ele[0] == "L":
            list_concat(out, lin_reg_letters(seq_list, 97, n))
        elif ele[0] == "N":
            list_concat(out, lin_reg_nums(seq_list, n))
    return out

# Combines values at each index of two same-length lists
def list_concat(l1, l2):
    if len(l1) == len(l2):
        for i in range(len(l1)):
            l1[i] = str(l1[i]) + str(l2[i])


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


# Builds a pattern definition string to support appropriate selection of
# regression types when matching patterns
def build_type(inp_string):
    inp_type = ""
    while inp_string != "":
        m = re.search('^[0-9]+', inp_string)
        if m is not None:
            inp_type += "N"
            inp_string = re.sub(r'^[0-9]+', "", inp_string, 1)
        m = re.search('^[A-Z]', inp_string)
        if m is not None:
            inp_type += "C"
            inp_string = re.sub(r'^[A-Z]', "", inp_string, 1)
        m = re.search('^[a-z]', inp_string)
        if m is not None:
            inp_type += "L"
            inp_string = re.sub(r'^[a-z]', "", inp_string, 1)
    return inp_type


if __name__ == '__main__':
    seq_list = get_user_pattern()
    seq_type = ""
    seq_valid = True
    for pos in range(len(seq_list)):
        if seq_type == "":
            seq_type = build_type(seq_list[pos])
        else:
            seq_valid = seq_type == build_type(seq_list[pos])
    if seq_valid:
        print(generate_predictions(parse_pattern(seq_type, seq_list), 5))
