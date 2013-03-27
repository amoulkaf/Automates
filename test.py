import automaton

def automate():
    
    alphabet = ['a', 'b']
    epsilons = []
    states = [0,1, 2,3,4,5,6] 
    initials = [0] 
    finals = [0,3,4,6,7]
    transitions=[
    (0,'a',2), (0,'b',1), (1,'b',1), (1,'a',2), (2,'b',2), (2,'a',3),
    (3,'a',2), (3,'b',6), (7,'b',3), (6,'b',7), (6,'a',5), (5,'a',6),
    (5,'b',5), (7,'a',5), (4,'a',5), (4,'b',4), (2,'b',2)
    ]
    return automaton.automaton(
    alphabet, epsilons, states, initials, finals, transitions
    )

def automate2():
    
    alphabet = ['a', 'b', 'c']
    epsilons = ['0']
    states = ['X', 'Y', 'Z'] 
    initials = ['X', 'Z'] 
    finals = ['Z']
    transitions=[
    ('X','a','X'),('X','c','X'), ('X','b','Y'), ('Y','c','X'), ('Y','b','Y'), ('Y','a','Z'), ('Z','a','Z'), ('Z','c','Z'), ('Z','b','Z'),('X','a','Y')
    ]
    return automaton.automaton(
    alphabet, epsilons, states, initials, finals, transitions
    )
B = automate( )
B.display()

