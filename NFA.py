import copy

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self._states = states
        self._alphabet = alphabet
        self._transitions = transitions
        self._start_state = start_state
        self._accept_states = accept_states
    def handle_lambda_moves(self, current_states):
        unexplored = copy.deepcopy(current_states)
        explored = []
        while len(unexplored) > 0:
            for state in unexplored:
                if (state, '') in self._transitions:
                    list_of_moves = self._transitions[(state, '')]
                    for move in list_of_moves:
                        if move not in explored and move not in unexplored:
                            unexplored.append(move)
                unexplored.remove(state)
                if (state not in explored):
                    explored.append(state)
        for explored_state in explored:
            if explored_state not in current_states:
                current_states.append(explored_state)
        return current_states
    def accepts(self, string_to_check):
        # Start with the start state
        current_states = [self._start_state]
        current_states = self.handle_lambda_moves(current_states)
        # For each letter in the input
        for letter in string_to_check:
            current_states = self.handle_lambda_moves(current_states)
            print("current states is ")
            print(current_states)
            copy_of_curr_states = copy.deepcopy(current_states)
            # For each state that we're at
            for state in copy_of_curr_states:
                # Remove the current state (may re-add if necessary)
                current_states.remove(state)
                # If there is a transition for that letter at that state
                if (state, letter) in self._transitions:
                    # Then add the result of the transition to current states
                    current_states = current_states + self._transitions[(state, letter)]
        current_states = self.handle_lambda_moves(current_states)
        # No more string input, so check if any current states are success states
        for state in current_states:
            if state in self._accept_states:
                return True
        return False
