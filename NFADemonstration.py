from NFA.py import NFA

newNFA = NFA(
["a", "b"], # States
[0, 1], # Alphabet
{("a", 0): "b", ("b", 0) : "a", ("a", 1) : "a", ("b", 1): "b"}, # Transitions
"a", # Start state
["b"] # Accept states
);

print(newNFA.accepts("00"))
