import qiskit.qasm3

program = """OPENQASM 3.0;
    include "stdgates.inc";
    bit[2] Bits;
    qubit[2] Qubits;
    h Qubits[0];
    cz Qubits[0], Qubits[1];
    barrier Qubits[0], Qubits[1];
    Bits[0] = measure Qubits[0];
    Bits[1] = measure Qubits[1];"""
    
circuit_1 = qiskit.qasm3.loads(program)
circuit_2 = qiskit.qasm3.load("Bell_state_circuit.qasm")

circuit_1.draw('mpl', style='iqx', filename='bell_state_circuit_1.png')
circuit_2.draw('mpl', style='iqx', filename='bell_state_circuit_2.png')