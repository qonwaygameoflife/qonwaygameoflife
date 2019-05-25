import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity

def liveliness(nhood):
    v=nhood
    a = v[0][0][0]+v[0][1][0]+v[0][2][0]+v[1][0][0]+v[1][2][0]+v[2][0][0]+v[2][1][0]+v[2][2][0]
    
    return a



def SQGOL(nhood):
    a = liveliness(nhood)
    value =  nhood[1][1]
    alive = np.array([0.0,1.0])
    dead = np.array([1.0,0.0])
    B = np.array([[0,0],[1,1]])
    D = np.array([[1,1],[0,0]])
    S = np.array([[1,0],[0,1]])
    if a <= 1:
        value =  dead
    elif (a > 1 and a <= 2):
        value = ((np.sqrt(2)+1)*2-(np.sqrt(2)+1)*a)*dead+(a-1)*value#(((np.sqrt(2)+1)*(2-a))**2+(a-1)**2)
    elif (a > 2 and a <= 3):
        value = (((np.sqrt(2)+1)*3)-(np.sqrt(2)+1)*a)*value+(a-2)*alive#(((np.sqrt(2)+1)*(3-a))**2+(a-2)**2)
    elif (a > 3 and a < 4):
        value = ((np.sqrt(2)+1)*4-(np.sqrt(2)+1)*a)*alive+(a-3)*dead#(((np.sqrt(2)+1)*(4-a))**2+(a-3)**2)
    elif a >= 4:
        value = dead
    value = value/np.linalg.norm(value)
    return value 

def DSQGOL(nhood):
    a = liveliness(nhood)
    value =  nhood[1,1]
    alive = [0,1]
    dead = [1,0]
    if value[1] > 0.98:
        if (a < 1 ):
            value = dead
        elif (a > 1 and a <= 1.5):
            value = dead
        elif (a > 1.5 and a <= 2.5):
            value = 0
        elif (a > 2.5 and a <= 3.5):
            value = 0
        elif (a > 3.5 and a <= 4.5):
            value = 0
        elif (a > 4.5):
            value = dead
    elif value[1] < 0.02:
        if (a < 1 ):
            value = dead
        elif (a > 1 and a <= 1.5):
            value = dead
        elif (a > 1.5 and a <= 2.5):
            value = 0
        elif (a > 2.5 and a <= 3.5):
            value = 0
        elif (a > 3.5 and a <= 4.5):
            value = 0
        elif (a > 4.5):
            value = dead   
    else:
        if (a < 1 ):
            value = dead
        elif (a > 1 and a <= 1.5):
            value = dead
        elif (a > 1.5 and a <= 2.5):
            value = 0
        elif (a > 2.5 and a <= 3.5):
            value = 0
        elif (a > 3.5 and a <= 4.5):
            value = 0
        elif (a > 4.5):
            value = dead     
    
