# Final project for Intro to Theory of Computation

## Example of usage

NFA that accepts a string with an odd number of zeroes.

Creation of object  
`newNFA = NFA(`  
`["a", "b"], // States`  
`[0, 1], //Alphabet`  
`{("a", 0): "b", ("b", 0) : "a", ("a", 1) : "a", ("b", 1): "b"}, //Transition function`  
`"a", //Start state`  
`["b"] //Accept states`  
`);`

Command line example  
`python3 NFAInterface.py 00 < ./test_cases/OddZeroes.txt`
