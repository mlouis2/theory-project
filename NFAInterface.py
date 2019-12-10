import sys
from NFA import NFA

def main():
    if len(sys.argv) is not 2:
        print("Requires exactly one command line arguments, a string.")
        return None
    string_to_check = sys.argv[1]

    lines = sys.stdin.readlines()

    start_state = lines[0].split("=")[1]
    start_state = start_state.rstrip()

    accept_states = []
    if "ACCEPT" in lines[1]:
        accept_states = lines[1].split("=")[1].split(",")
        # Remove trailing whitespace
        accept_states = [str.rstrip() for str in accept_states]

    states = list(start_state) + list(accept_states)
    alphabet = []
    transitions = {}

    remaining_lines = lines[2:] if len(accept_states) > 0 else lines[1:]
    for line in remaining_lines:
        lhs, rhs = line.split("->")
        rhs = rhs.rstrip()
        from_state = ""
        machine_input = ""
        if ":" in lhs:
            from_state, machine_input = lhs.split(":")
            from_state = from_state.rstrip()
            if machine_input not in alphabet:
                alphabet.append(machine_input)
        else:
            from_state = lhs
            from_state = from_state.rstrip()
        if from_state not in states:
            states.append(from_state)
        if rhs not in states:
            states.append(rhs)
        if (from_state, machine_input) in transitions:
            transitions[(from_state, machine_input)].append(rhs)
        else:
            transitions[(from_state, machine_input)] = [rhs]

    machine = NFA(states, alphabet, transitions, start_state, accept_states)

    if (machine.accepts(string_to_check)):
        print('The machine accepts "' + string_to_check + '".')
        return True
    else:
        print('The machine does not accept "' + string_to_check + '".')
        return False

if __name__ == "__main__":
    main()
