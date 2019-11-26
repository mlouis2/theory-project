import copy

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    def accepts(self, str):
        # Start with the start state
        current_states = [self.start_state]
        if (self.start_state, '') in self.transitions:
            current_states = current_states + self.transitions[(self.start_state, '')]
        # For each letter in the input
        for letter in str:
            for state in current_states:
                if (state, '') in self.transitions:
                    current_states = current_states + self.transitions[(state, '')]
            copy_of_curr_states = copy.deepcopy(current_states)
            # For each state that we're at
            for state in copy_of_curr_states:
                # Remove the current state (may re-add if necessary)
                current_states.remove(state)
                # If there is a transition for that letter at that state
                list = [state, letter]
                if tuple(list) in self.transitions:
                    # Then add the result of the transition to current states
                    current_states = current_states + self.transitions[(state, letter)]
        # No more string input, so check if any current states are success states
        for state in current_states:
            if state in self.accept_states:
                return True
        return False
