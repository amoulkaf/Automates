import automaton

def automate2():
    
    alphabet = ['a', 'b', 'c']
    epsilons = ['0']
    states = ['X', 'Y', 'Z'] 
    initials = ['X'] 
    finals = ['Z']
    transitions=[
    ('X','a','X'),('X','c','X'), ('X','b','Y'), ('Y','c','X'), ('Y','b','Y'), ('Y','a','Z'), ('Z','a','Z'), ('Z','c','Z'), ('Z','b','Z')
    ]
    return automaton.automaton(
    alphabet, epsilons, states, initials, finals, transitions
    )
B = automate2( )
B.display()

