#!/usr/bin/env python3


import math

from neighbours import neighbours3
from qiskit import QuantumCircuit
from qiskit import Aer, execute
from qiskit.aqua.components.oracles import TruthTableOracle
from qiskit.circuit.reset import reset
from qiskit.extensions.standard import barrier, h, swap, x

def make_init_circuit(register, init_cells):
    init_circuit = QuantumCircuit(register)
    for i, v in enumerate(init_cells[::-1]):
        if v == '0':
            continue

        if v == '1':
            init_circuit.x(register[i])
        else:
            init_circuit.h(register[i])

    return init_circuit

def make_barrier_circuit(regs):
    circuit = QuantumCircuit(*regs)
    for r in regs:
        circuit.barrier(r)

    return circuit

def make_swap_circuit(reg01, reg02):
    circuit = QuantumCircuit(reg01, reg02)
    circuit.swap(reg01, reg02)

    return circuit

def make_reset_circuit(regs):
    circuit = QuantumCircuit(*regs)
    for r in regs:
        circuit.reset(r)

    return circuit

def make_oracle(qcount):
    bitmaps = [''] * qcount

    for raw_value in range(2**qcount):
        value = format(raw_value, '0{}b'.format(qcount))[::-1]
    
        for index in range(qcount):
            n = neighbours3(index, value)
    
            alive_count = 1 if n[0] == '1' else 0
            alive_count += 1 if n[2] == '1' else 0
    
            if n[1] == '0' and alive_count == 2:
                bitmaps[index] += '1'
            elif n[1] == '1' and alive_count == 1:
                bitmaps[index] += '1'
            else:
                bitmaps[index] += '0'

    return TruthTableOracle(bitmaps)

def vector_state_to_summary(state, extract_cells):
    summary = {}

    circuit_size = int(math.log(len(state), 2))
    for index, value in enumerate(state):
        if value == complex(0,0):
            continue

        f_index = format(index, '0{}b'.format(circuit_size))

        cells = extract_cells(f_index)

        if cells in summary:
            summary[cells] += value
        else:
            summary[cells] = value

    return summary

def print_summary(summary, min_prob):
    for cells, value in summary.items():
        prob = abs(value)

        if prob >= min_prob:
            print('{}  <{}>'.format(format_cells(cells), prob))

def print_cells(cells):
    print(format_cells(cells))

def format_cells(cells):
    output = ''
    for c in cells:
        if c == '0':
            output += '□'
        elif c == '1':
            output += '■'
        else:
            output += '☒'

    return ' '.join(output)

init_cells = 'XXX'
print('Input:')
print_cells(init_cells)

qcount = len(init_cells)
oracle = make_oracle(qcount)

oracle_circuit = oracle.construct_circuit()
init_circuit = make_init_circuit(oracle.variable_register, init_cells)
circuit = init_circuit + oracle_circuit

backend_sim = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend_sim).result()
state = result.get_statevector(circuit)

cell_range_start = oracle.ancillary_register.size
cell_range_end = cell_range_start + oracle.output_register.size
extract_cells = lambda index: index[cell_range_start:cell_range_end]
summary = vector_state_to_summary(state, extract_cells)

print('Output:')
min_prob = 0 #(1 / len(summary)) - 0.00001
print_summary(summary, min_prob)

oracle2 = make_oracle(qcount)

oracle2_circuit = oracle2.construct_circuit()
barrier_circuit = make_barrier_circuit(oracle2_circuit.qregs)
swap_circuit = make_swap_circuit(oracle.output_register,
                                 oracle2.variable_register)
reset_circuit = make_reset_circuit([oracle2.output_register, oracle2.ancillary_register])
circuit2 = (init_circuit + oracle_circuit +
            barrier_circuit + swap_circuit + reset_circuit + oracle2_circuit)
##print(circuit2)

result = execute(circuit2, backend_sim).result()
state = result.get_statevector(circuit2)

cell_range_start = oracle2.ancillary_register.size
cell_range_end = cell_range_start + oracle2.output_register.size
extract_cells = lambda index: index[cell_range_start:cell_range_end]
summary = vector_state_to_summary(state, extract_cells)

print('Output:')
min_prob = 0 #(1 / len(summary)) - 0.00001
print_summary(summary, min_prob)
