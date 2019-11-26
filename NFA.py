class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        print(self.states)
        print(self.alphabet)
        print(self.transitions)
        print(self.start_state)
        print(self.accept_states)
    def accepts(str):
        return True
