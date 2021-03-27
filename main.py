from scipy import stats

# Python tester program to take in a pattern
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


# Takes in a sequence of numbers and returns the next n predicted elements
def lin_reg_nums(inp_list, n):
    sz = len(inp_list)
    xs = range(sz)
    res = stats.linregress(xs, inp_list)
    for x in range(n):
        print(int(res.intercept + res.slope * (sz + x)))


if __name__ == '__main__':
    allNums = True
    seq_list = get_user_pattern()
    for i in range(len(seq_list)):
        if not seq_list[i].isdigit():
            allNums = False
        else:
            seq_list[i] = int(seq_list[i])
    if allNums:
        lin_reg_nums(seq_list, 5)
    else:
        print("Please enter only numbers.")
