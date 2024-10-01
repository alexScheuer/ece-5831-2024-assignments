import numpy as np

class LogicGate():
    def __init__(self):
        pass

    #First is an AND gate, whose truth table should be:
    #x1 && x2    result
    #0     0     0
    #1     0     0
    #0     1     0
    #1     1     1
    def and_gate(self, x1, x2):
        b = 1.9
        w = np.array([1, 1, 1])
        x = np.array([x1, x2, b])
        if(w1*x1 + w2*x2) > b:
            return 1
        else:
            return 0


    #Next a NAND gate, just the AND gate negated, truth table:
    #x1 && x2    result
    #0     0     1
    #1     0     1
    #0     1     1
    #1     1     0
    def nand_gate(self, x1, x2):
        b = 1.9
        w = np.array([-0.5, -0.5, 1])
        x = np.array([x1, x2, b])
        if(w1*x1 + w2*x2) > b:
            return 1
        else:
            return 0


    #Now an OR gate, truth table:
    #x1 && x2    result
    #0     0     0
    #1     0     1
    #0     1     1
    #1     1     1
    def or_gate(self, x1, x2):
        b = 0.2
        w = np.array([0.3, 0.3, 1])
        x = np.array([x1, x2, b])
        if(w1*x1 + w2*x2) > b:
            return 1
        else:
            return 0


    #Now an NOR gate, negated OR:
    #x1 && x2    result
    #0     0     1
    #1     0     0
    #0     1     0
    #1     1     0
    def nor_gate(self, x1, x2):
        b = -0.3
        w = np.array([-0.4, -0.4, 1])
        x = np.array([x1, x2, b])
        if(w1*x1 + w2*x2) > b:
            return 1
        else:
            return 0


    #Lastly the XOR gate, truth table:
    #x1 && x2    result
    #0     0     0
    #1     0     1
    #0     1     1
    #1     1     0
    def xor_gate(self, x1, x2):
        b1 = 0.7
        b2 = 1.5
        w = np.array([0.9, 0.9, 1, 1])
        x = np.array([x1, x2, b1, b2])
        if(w1*x1 + w2*x2) > b:
            return 1
        else:
            return 0
