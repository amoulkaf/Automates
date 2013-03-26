1import automaton


def automate():
    
    alphabet = ['a', 'b']
    epsilons = ['0']
    states = [1, 2] 
    initials = [1] 
    finals = [2]
    transitions=[
    (1,'b',1), (1,'a',1), (1,'c',2), (2,'a',2), (2,'b',2), (2,'c',2)
    ]
    return automaton.automaton(
    alphabet, epsilons, states, initials, finals, transitions
    )
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
    alphabet, epsilons, states, initials, finals, transitions)
    
def mirror(a):
    self = automaton.automaton(
        alphabet = a.get_alphabet(),
        epsilons = a.get_epsilons(),
        states = a.get_states(),
        initials = a.get_final_states(),
        finals = a.get_initial_states(),     
        )
    transitions = a.get_transitions()
    for t in transitions:
        self.add_transition((t[2], t[1], t[0]))
    return self

def complement(a):
    found = False
    complet = True
    comp = a.clone()
    states = a.get_states()
    transitions = a.get_transitions()
    alphabet = a.get_alphabet()
    
    for e in states:
        for al in alphabet:
            for t in transitions:
                if (t[0] == e and t[1] == al):
                    found = True
            if found == False:
                complet = False
                comp.add_transition((e, al, 'p'))
            found = False
        
    if complet == False:
        comp.add_state('p')
        for al in alphabet:
            comp.add_transition(('p', al, 'p'))

    return comp

def union_intersection_aux(auto1, auto2):
    
    self = automaton.automaton()
    transitions1 = auto1.get_transitions()
    transitions2 = auto2.get_transitions()
    
    for t1 in transitions1:
        for t2 in transitions2:
            if t1[1] == t2[1]:
                self.add_transition(((t1[0], t2[0]), t1[1] ,(t1[2], t2[2])))
                if not(self.has_state((t1[0], t2[0]))):
                    self.add((t1[0], t2[0]))
                if not(self.has_state((t1[2], t2[2]))):
                    self.add((t1[2], t2[2]))
                if auto1.state_is_initial(t1[0]) and auto2.state_is_initial(t2[0]):
                    self.add_initial_state((t1[0], t2[0]))
    return self

def union(auto1, auto2):
    
    self = union_intersection_aux(auto1, auto2)
    
    for s in self.get_states():
        if auto1.state_is_final(s[0]) or auto2.state_is_final(s[1]):
            self.add_final_state((s[0], s[1]))
    
    return self

def intersection(auto1, auto2):
    
    self = union_intersection_aux(auto1, auto2)
    
    for s in self.get_states():
        if auto1.state_is_final(s[0]) and auto2.state_is_final(s[1]):
            self.add_final_state((s[0], s[1]))
    
    return self

B = automate2( )
C = automate( )
self = intersection(B,C)
self.display()


