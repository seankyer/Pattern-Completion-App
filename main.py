from scipy import stats
import requests

# Python tester program to take in a pattern
# and return a prediction of the next n elements


# Prompts the user to input a sequence of data and terminates on 'exit'
def get_user_pattern():
    inp_list = []
    latest_input = 'qwer'
    print("please enter your pattern element, return with empty string when done\n")
    while latest_input != '':
        if latest_input != 'qwer':
            inp_list.append(latest_input)
        latest_input = input("input" + str(len(inp_list))+ ":")
    return inp_list


# Takes in a sequence of numbers and returns the next n predicted elements
def lin_reg_nums(inp_list, n):
    sz = len(inp_list)
    xs = range(sz)
    slope, intercept, r, p, se = stats.linregress(xs, inp_list)
    for x in range(n):
        print(int(intercept + slope * (sz + x)))

def data_muse_simple(input, index, n):
    for x in range(len(index)):
        response = requests.get("https://api.datamuse.com/words?rel_trg=" + input[index[x]])
        print(str(n) + " words after the word " + input[index[x]] + " is:")
        for i in range(n):
            print(response.json()[i]["word"])


if __name__ == '__main__':
    # allNums = True
    # reponse = requests.get("https://api.datamuse.com/words?rel_trg=" + "banana")
    # print(response.json())
    strings_index = []
    seq_list = get_user_pattern()
    for i in range(len(seq_list)):
        if not seq_list[i].isdigit():
            allNums = False
            strings_index.append(i)
        else:
            seq_list[i] = int(seq_list[i])
    if allNums:
        lin_reg_nums(seq_list, 5)
    else:
        data_muse_simple(seq_list, strings_index, 5)
        # print("Please enter only numbers.")