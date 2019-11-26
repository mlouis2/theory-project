import sys
from NFA import NFA

if len(sys.argv) is not 3:
    print("Requires exactly two command line arguments, a file path to an NFA "
    + "description and a string.")
else:
    file_path = sys.argv[1]
    string_to_check = sys.argv[2]

    file = open(file_path)
    lines = file.readlines()

    start_state = lines[0].split("=")[1]
    start_state = start_state.rstrip()

    accept_states = lines[1].split("=")[1].split(",")
    # Remove trailing whitespace
    accept_states = [str.rstrip() for str in accept_states]

    states = list(start_state) + list(accept_states)
    alphabet = []
    transitions = {}

    for line in lines[2:]:
        lhs, rhs = line.split("->")
        rhs = rhs.rstrip()
        from_state = ""
        input = ""
        if ":" in lhs:
            from_state, input = lhs.split(":")
            from_state = from_state.rstrip()
            if input not in alphabet:
                alphabet.append(input)
        else:
            from_state = lhs
            from_state = from_state.rstrip()
        if from_state not in states:
            states.append(from_state)
        if rhs not in states:
            states.append(rhs)
        if (from_state, input) in transitions:
            transitions[(from_state, input)].append(rhs)
        else:
            transitions[(from_state, input)] = [rhs]

    machine = NFA(states, alphabet, transitions, start_state, accept_states)

    if (machine.accepts(string_to_check)):
        print("The machine accepts \"" + string_to_check + "\".")
    else:
        print("The machine does not accept \"" + string_to_check + "\".")
