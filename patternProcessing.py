import numpy as np
import re


def parse_pattern(s_t, pat):
    p = pat.copy()
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
            elif s_t[n] == "S":
                mat = re.search('^[^A-Za-z0-9]+', p[m])
                pattern_arr[n].append(mat.group(0))
                p[m] = re.sub(r'^[^A-Za-z0-9]+', "", p[m], 1)
    return pattern_arr


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
        m = re.search('^[^A-Za-z0-9]+', inp_string)
        if m is not None:
            inp_type += "S"
            inp_string = re.sub(r'^[^A-Za-z0-9]+', "", inp_string, 1)
    return inp_type


def is_valid_seq(seq_mat):
    seq_list = np.array(seq_mat).copy().flatten()
    seq_type = ""
    for pos in range(len(seq_list)):
        if seq_type == "":
            seq_type = build_type(seq_list[pos])
        elif seq_type != build_type(seq_list[pos]):
            return False
    return seq_type


def special_is_const(seq_list):
    return seq_list.count(seq_list[0]) == len(seq_list)
