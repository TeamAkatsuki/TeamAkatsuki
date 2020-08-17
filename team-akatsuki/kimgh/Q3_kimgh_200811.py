# palindrome


def palinum(p_str):
    rev_str = ''
    for i in range(len(p_str)):
        rev_str += p_str[-i-1]
    if rev_str == p_str:
        return p_str


print(palinum('abccba'))
