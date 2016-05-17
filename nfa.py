from postfix import *


class State:
    def __init__(self, label='', has_label=False, split=False, match=False, out1=None, out2=None):
        self.label = label
        self.has_label = has_label
        self.split = split
        self.match = match
        self.out1 = out1
        self.out2 = out2

    def patch(self, next_state):
        if self.out1 is None:
            self.out1 = next_state
        if self.out2 is None:
            self.out2 = next_state


class Fragment:
    def __init__(self, start=None, out_states=[]):
        self.start = start
        self.out_states = out_states


class NFA:
    def __init__(self):
        pass

    def post_2_nfa(self, reg):
        post_reg = Postfix().in_2_post(reg)
        fragments = []
        for char in post_reg:
            if self._is_literal(char):
                literal_state = State(char, True)
                fragments.append(Fragment(literal_state, [literal_state]))
            elif self._is_star(char):
                previous = fragments.pop()
                star_state = State(out1=previous)
                self._patch(previous, star_state)
                fragments.append(Fragment(star_state, [star_state]))
            elif self._is_concatenation(char):
                previous = fragments.pop()
                prev_previous = fragments.pop()
                self._patch(prev_previous, previous.start)
                fragments.append(Fragment(prev_previous.start, previous.out_states))
            elif self._is_plus(char):
                pass
            elif self._is_question_mark(char):
                pass

        match_state = State(match=True)
        nfa = fragments.pop()
        self._patch(nfa, match_state)
        return nfa.start

    def _patch(self, fragment, state):
        for state_in_frag in fragment.out_states:
            state_in_frag.patch(state)

    def _is_star(self, char):
        return char == '*'

    def _is_concatenation(self, char):
        return char == '#'

    def _is_plus(self, char):
        return char == '+'

    def _is_question_mark(self, char):
        return char == '?'

    def _is_literal(self, char):
        return not self._is_star(char) and not self._is_concatenation(char) \
               and not self._is_plus(char) and not self._is_question_mark(char)