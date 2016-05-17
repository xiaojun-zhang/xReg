from nfa import *

def match(reg, str):
    nfa = NFA().post_2_nfa(reg)


if __name__ == '__main__':
    match('ab*', 'ab')