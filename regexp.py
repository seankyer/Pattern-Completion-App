from dataclasses import dataclass
# basically python structs

@dataclass
class WordPiece:
    typename: str           # "uppercase", "lowercase", "special", or "number"
    constant: bool          # true if all strings have it
    length: int             # general length
    length_plus: int = 0    # Additional length if this applies to multiple words 


def get_regexp(inputs):
    return "";

# written at 1am 
# literally unreadable
def break_word(word):
    pieces = []
    i = 0
    while i < len(word):
        ct = chartype(word[i])
        wp = WordPiece(ct, False, 1)
        i+=1
        # print(i, "what", wp)
        if i >= len(word):
            pieces.append(wp)
            break
        while chartype(word[i]) == ct:
            # print(i, "what", wp)
            wp.length += 1
            i += 1
            if i >= len(word):
                pieces.append(wp)
                break 
            elif (chartype(word[i]) != ct):
                pieces.append(wp)
    return pieces
        

def chartype(char):
    if char.isnumeric():
        return "number"
    elif char.isalnum():
        if char.isupper():
            return "uppercase"
        else: 
            return "lowercase"
    else :
        return "special"


if __name__ == '__main__':
    args = []
    while True:
        userIn = input("Add to list: ")
        args.append(userIn)
        if userIn == "":
            break
    
    # print("regexp: ", get_regexp(args))
    print(break_word("WHATwhat123..."))