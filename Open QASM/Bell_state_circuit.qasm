OPENQASM 3.0;
include "stdgates.inc";
bit[2] Bits;
qubit[2] Qubits;
h Qubits[0];
cz Qubits[0], Qubits[1];
barrier Qubits[0], Qubits[1];
Bits[0] = measure Qubits[0];
Bits[1] = measure Qubits[1];
