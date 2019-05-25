import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity

def liveliness(nhood):
    a=0
    for i, v in enumerate(nhood):
        if i != 5:
            a+=v[1]
    return a

def SQGOL(a, nhood):
    value =  nhood[1,1]
    alive = [0,1]
    dead = [1,0]
    B = np.array([[0,0],[1,1]])
    D = np.array([[1,1],[0,0]])
    S = np.array([[1,0],[0,1]])
    if a =< 1:
        value =  alive
    elif (a > 1 and a <= 2):
        value = (np.sqrt(2)+1)(2-a)*alive+(a-1)*value
    elif (a > 2 and a <= 3):
        value = (np.sqrt(2)+1)(3-a)*value+(a-2)*alive
    elif (a > 3 and a <= 4):
        value = (np.sqrt(2)+1)(4-a)*alive+(a-3)*dead
    else :
        value = dead
    return value 

def DSQGOL(a,nhood):
    value =  nhood[1,1]
    alive = [0,1]
    dead = [1,0]
    if (a > 1 and a <= 1.5):
        value = dead
    