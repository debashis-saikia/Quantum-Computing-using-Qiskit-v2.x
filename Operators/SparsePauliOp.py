import qiskit
import numpy
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import PauliGate
import pylatexenc

# SparsePauliOp.from_sparse_pauli(['Operator', [qubit index], coefficient], num_qubits = )
operator_1 = SparsePauliOp.from_sparse_list([('X', [2], 1.0 + 1.0j), ('Z', [0], 0.5), ('Y', [1], 0.4 + 0.2j), ('Z', [0], 0.2)], num_qubits= 4)
print(f'operator_1: {operator_1}')


# Another method without from_pauli_list()
paulis = ["IIXX", "IXXI", "XXII", "ZIIZ"]
coeffs = [1.0 + 1.0j, 1.0 + 1.0j, 0. + 1.0j, 1.0 + 0.0j]

operator_2 = SparsePauliOp(paulis, coeffs) 
print(f'operator_2: {operator_2}')

operator_3 = operator_2 @ operator_1
print(f'operator_3: {operator_3}')

operator_4 = operator_1.tensor(operator_2)
print(f'operator_4: {operator_4}')

num_qubits = operator_4.num_qubits # Extracting the number of qubits in the operator.
qc = qiskit.QuantumCircuit(num_qubits)

for pauli in operator_4.paulis:
    pauli_str = pauli.to_label() # Extracting the Pauli object. And  converting them to string.
    gate = PauliGate(pauli_str)  # Converting pauli string to quantum gate.
    qc.append(gate, range(num_qubits)) # Appending quantum gate to the Quantum Circuit
print(qc.draw())
qc.draw('mpl', style = 'clifford')

