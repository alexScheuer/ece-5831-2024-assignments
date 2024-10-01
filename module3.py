import numpy as np

import logic_gate as lg

logic_gate = lg.LogicGate()


#this will only run if this module is called via the command line:
def print_help():
    print("LogicGate Class Usage:")
    print("- Use LogicGate().and_gate(x1, x2)  for AND  gate simulation")
    print("- Use LogicGate().nand_gate(x1, x2) for NAND gate simulation")
    print("- Use LogicGate().or_gate(x1, x2)   for OR   gate simulation")
    print("- Use LogicGate().nor_gate(x1, x2)  for NOR  gate simulation")
    print("- Use LogicGate().xor_gate(x1, x2)  for XOR  gate simulation")
    print("\nExample usage:")
    print("lg = LogicGate()")
    print("result = lg.and_gate(1, 1)")
    print("print(result)")

if __name__ == "__main__":
    import sys

    # If called via command line, show help messages automatically
    if len(sys.argv) == 1:
        print("No command-line arguments provided. Showing help:")
        print_help()
##################################################


#testing AND gate
print("First we will test the AND gate, using the following truth table:")
print("x1    x2    result")
print("0     0     0")
print("1     0     0")
print("0     1     0")
print("1     1     1")
print("The resulting values are:")
r = logic_gate.and_gate(0, 0)
print(r)
r = logic_gate.and_gate(1, 0)
print(r)
r = logic_gate.and_gate(0, 1)
print(r)
r = logic_gate.and_gate(1, 1)
print(r)
print()

#testing NAND gate
print("Next we will test the NAND gate, using the following truth table:")
print("x1    x2    result")
print("0     0     1")
print("1     0     1")
print("0     1     1")
print("1     1     0")
print("The resulting values are:")
r = logic_gate.nand_gate(0, 0)
print(r)
r = logic_gate.nand_gate(1, 0)
print(r)
r = logic_gate.nand_gate(0, 1)
print(r)
r = logic_gate.nand_gate(1, 1)
print(r)
print()

#testing OR gate
print("Next we will test the OR gate, using the following truth table:")
print("x1    x2    result")
print("0     0     0")
print("1     0     1")
print("0     1     1")
print("1     1     1")
print("The resulting values are:")
r = logic_gate.or_gate(0, 0)
print(r)
r = logic_gate.or_gate(1, 0)
print(r)
r = logic_gate.or_gate(0, 1)
print(r)
r = logic_gate.or_gate(1, 1)
print(r)
print()

#testing the NOR gate
print("Next we will test the NOR gate, using the following truth table:")
print("x1    x2    result")
print("0     0     1")
print("1     0     0")
print("0     1     0")
print("1     1     0")
print("The resulting values are:")
r = logic_gate.nor_gate(0, 0)
print(r)
r = logic_gate.nor_gate(1, 0)
print(r)
r = logic_gate.nor_gate(0, 1)
print(r)
r = logic_gate.nor_gate(1, 1)
print(r)
print()

#testing the XOR gate:
print("Lastly we will test the XOR gate, using the following truth table:")
print("x1    x2    result")
print("0     0     0")
print("1     0     1")
print("0     1     1")
print("1     1     0")
print("The resulting values are:")
r = logic_gate.xor_gate(0, 0)
print(r)
r = logic_gate.xor_gate(1, 0)
print(r)
r = logic_gate.xor_gate(0, 1)
print(r)
r = logic_gate.xor_gate(1, 1)
print(r)
print()
