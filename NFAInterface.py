import sys

if len(sys.argv) is not 3:
    print("Requires exactly two command line arguments, a file path to an NFA "
    + "description and a string.")
else:
    file_path = sys.argv[1]
    string_to_check = sys.argv[2]

    file = open(file_path)
    lines = file.readlines()
    
    start_state = lines[0].split("=")[1]

    accept_states = lines[1].split("=")[1].split(",")
    # Remove trailing whitespace
    accept_states = [str.rstrip() for str in accept_states]

    for line in lines[2:]:
        print("")
