import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity

def liveliness(nhood):
    a=0.0
    for i, v in enumerate(nhood):
        if i != 5:
            a+=v[0][1]
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
        value =  alive
    elif (a > 1 and a <= 2):
        value = (np.sqrt(2)+1)*(2-a)*alive+(a-1)*value
    elif (a > 2 and a <= 3):
        value = (np.sqrt(2)+1)*(3-a)*value+(a-2)*alive
    elif (a > 3 and a <= 4):
        value = (np.sqrt(2)+1)*(4-a)*alive+(a-3)*dead
    else:
        value = dead
    value = value/np.linalg.norm(value)
    return value 

# def GOL1(value,a):
#     #a = liveliness(nhood)
#     #value =  nhood[1][1]
#     alive = np.array([0.0,1.0])
#     dead = np.array([1.0,0.0])
#     B = np.array([[0,0],[1,1]])
#     D = np.array([[1,1],[0,0]])
#     S = np.array([[1,0],[0,1]])
#     if a <= 1:
#         value =  alive
#     elif (a > 1 and a <= 2):
#         value = np.matmul((np.sqrt(2)-1)*(2-a)*D,value)+np.matmul((a-1)*S,value)
#     elif (a > 2 and a <= 3):
#         value = np.matmul((np.sqrt(2)-1)*(3-a)*S,value)+np.matmul((a-2)*B,value)
#     elif (a > 3 and a <= 4):
#         value = np.matmul(np.sqrt(2)-1*(4-a)*B,value)+np.matmul((a-3)*D,value)
#     else:
#         value = dead
#     return value 

# def GOL2(value,a):
#     #a = liveliness(nhood)
#     #value =  nhood[1][1]
#     alive = np.array([0.0,1.0])
#     dead = np.array([1.0,0.0])
#     B = np.array([[0,0],[1,1]])
#     D = np.array([[1,1],[0,0]])
#     S = np.array([[1,0],[0,1]])
#     if a <= 1:
#         value =  alive
#     elif (a > 1 and a <= 2):
#         value = (np.sqrt(2)+1)*(2-a)*np.matmul(D,value)+(a-1)*np.matmul(S,value)
#     elif (a > 2 and a <= 3):
#         value = (np.sqrt(2)+1)*(3-a)*np.matmul(S,value)+(a-2)*np.matmul(B,value)
#     elif (a > 3 and a <= 4):
#         value = (np.sqrt(2)+1)*(4-a)*np.matmul(B,value)+(a-3)*np.matmul(D,value)
#     else:
#         value = dead
#     return value 

# def GOL3(value,a):
#     #a = liveliness(nhood)
#     #value =  nhood[1][1]
#     alive = np.array([0.0,1.0])
#     dead = np.array([1.0,0.0])
#     B = np.array([[0,0],[1,1]])
#     D = np.array([[1,1],[0,0]])
#     S = np.array([[1,0],[0,1]])
#     if a <= 1:
#         value =  alive
#     elif (a > 1 and a <= 2):
#         value = (np.sqrt(2)+1)*(2-a)*dead+(a-1)*np.matmul(S,value)
#     elif (a > 2 and a <= 3):
#         value = (np.sqrt(2)+1)*(3-a)*np.matmul(S,value)+(a-2)*alive
#     elif (a > 3 and a <= 4):
#         value = (np.sqrt(2)+1)*(4-a)*alive+(a-3)*dead
#     else:
#         value = dead
#     value = value/np.linalg.norm(value)
#     print(np.linalg.norm(value))
#     return value 

def DSQGOL(a,nhood):
    value =  nhood[1,1]
    alive = [0,1]
    dead = [1,0]
    if (a < 1.5):
        value = 0
    elif (a > 1 and a <= 1.5):
        value = dead
    elif (a < 1.5 and a <= 2.5):
        value = 0
    
