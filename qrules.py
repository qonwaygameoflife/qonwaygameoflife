import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
from qiskit.tools.qi.qi import partial_trace

def liveliness(nhood):
    v=nhood
    a = v[0][0][0]+v[0][1][0]+v[0][2][0]+v[1][0][0]+v[1][2][0]+v[2][0][0]+v[2][1][0]+v[2][2][0]

    return a



def SQGOL(nhood):
    a = liveliness(nhood)
    value =  nhood[1][1]
    alive = np.array([1.0,0.0])
    dead = np.array([0.0,1.0])
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

def init_quantum(nhood):
    v=nhood
<<<<<<< HEAD
    a = (v[0][0]+v[0][1]+v[0][2]+v[1][0]+v[1][2]+v[2][0]+v[2][1]+v[2][2])/8
    a = a/np.linalg.norm(a)
=======
    av = (v[0][0]+v[0][1]+v[0][2]+v[1][0]+v[1][2]+v[2][0]+v[2][1]+v[2][2])/8
    print(av)
    av = av/np.linalg.norm(av)
>>>>>>> 53f6f358e693a66712f6c984395e7787c7fa4546
    qr = QuantumRegister(3,'qr')
    qc = QuantumCircuit(qr,name='conway')
    counter  = 0
    initial_state = (1/np.sqrt(6))*np.array([2,1,0,1])
    qc.initialize(initial_state,[qr[1],qr[2]])
<<<<<<< HEAD
    qc.initialize(a,[qr[0]])
    qc.cx(qr[0],qr[1])
=======
    qc.initialize(av,[qr[0]])
    qc.cx(qr[0],qr[1]) 
>>>>>>> 53f6f358e693a66712f6c984395e7787c7fa4546
    qc.cx(qr[0],qr[2])
    qc.cx(qr[1],qr[0])
    qc.cx(qr[2],qr[0])
    job = execute(qc,Aer.get_backend('statevector_simulator'))
    results = job.result().get_statevector()
<<<<<<< HEAD
    del qr
    del qc
    del job
    value = partial_trace(results,[1,2])[0]
    value = np.real(value)
=======
    value = partial_trace(results,[1,2])
    print(value)
>>>>>>> 53f6f358e693a66712f6c984395e7787c7fa4546
    return value

<<<<<<< HEAD



=======
      
>>>>>>> 53f6f358e693a66712f6c984395e7787c7fa4546

def DSQGOL(nhood):

    a = liveliness(nhood)
<<<<<<< HEAD
<<<<<<< HEAD
    
    value =  nhood[1][1][0]
=======
=======
>>>>>>> parent of 2181c44... Update qrules.py
    print(a)
    value =  nhood[1][1]
>>>>>>> parent of 2181c44... Update qrules.py
    alive = [1,0]
    dead = [0,1]
<<<<<<< HEAD

    if value[0] > 0.98:
        if (a < 1 ):
            value = dead
        elif (a > 1 and a <= 1.5):
=======
    
    if value > 0.98:
        if (a <= 1.5 ):
>>>>>>> 53f6f358e693a66712f6c984395e7787c7fa4546
            value = dead
        elif (a > 1.5 and a <= 2.5):
            print('here')
            value = init_quantum(nhood)
            # qci, qri = init_quantum(nhood)
            # for i in range(9):
            #     if i !=5:
            #         qci.cx(qri[5],qri[i])
            #     job = execute(qci,Aer.get_backend('statevector_simulator'))
            #     results = job.result().get_statevector()
            #     value = partial_trace(results,[0,1,2,3,4,6,7,8])
        elif (a > 2.5 and a <= 3.5):
            value = alive
        elif (a > 3.5):
            value = dead
    elif value < 0.02:
        if (a < 1 ):
            value = dead
        elif (a > 1 and a <= 1.5):
            value = dead
        elif (a > 1.5 and a <= 2.5):
            value = init_quantum(nhood)
            # qc, qr = init_quantum(nhood)
            # for i in range(9):
            #     if i !=5:
            #         qci.cx(qri[5],qri[i])
            #     job = execute(qc,Aer.get_backend('statevector_simulator'))
            #     results = job.result().get_statevector()
            #     value = partial_trace(results,[0,1,2,3,4,6,7,8])
        elif (a > 2.5 and a <= 3.5):
            value = alive
        elif (a > 3.5):
            value = dead
    else:
        if (a < 1 ):
            value = dead
        elif (a > 1 and a <= 1.5):
            value = dead
        elif (a > 1.5 and a <= 2.5):
            value = init_quantum(nhood)
            # qci, qri = init_quantum(nhood)
            # for i in range(9):
            #     if i !=5:
            #         qci.cx(qri[5],qri[i])
            #     job = execute(qc,Aer.get_backend('statevector_simulator'))
            #     results = job.result().get_statevector()
            #     value = partial_trace(results,[0,1,2,3,4,6,7,8])
        elif (a > 2.5 and a <= 3.5):
            value = init_quantum(nhood)
            # qri = QuantumRegister(1,'qr')
            # qci = QuantumCircuit(qc,name='conway')
            # qci.initialize(value,qri[i])
            # qci.measure(qr(5))
            # job = execute(qci,Aer.get_backend('statevector_simulator'))
            # value = job.result().get_statevector()
        elif (a > 3.5):
<<<<<<< HEAD
            value=dead
=======
            value=dead    
        print(value) 
        value = np.array([1.,0.])
>>>>>>> 53f6f358e693a66712f6c984395e7787c7fa4546
    return value
