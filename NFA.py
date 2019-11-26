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
        # For each letter in the input
        for letter in str:
            # For each state that we're at
            for state in current_states:
                # Remove the current state (may re-add if necessary)
                current_states.remove(state)
                # If there is a transition for that letter at that state
                if (state, letter) in self.transitions:
                    # Then add the result of the transition to current states
                    current_states.append(self.transitions[(state, letter)])
                # Handle lambda moves
                if (state, '') in self.transitions:
                    current_states.append(self.transitions[(state, '')])

                # For state in current states
                    # If no transition available, remove it from current states
                    # If transition available, replace that state with the new state in
                    #   current states.
                    # Also check for lambda moves.
                # When no more string input, check if any of current states are success
                # states.
        return True
