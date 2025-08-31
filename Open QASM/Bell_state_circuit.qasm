OPENQASM 3.0;
include "stdgates.inc"
bits[2] Bits;
qubits[2] Qubits;
h Qubits[0];
cz Qubits[0], Qubits[1];
barrier Qubits[0], Qubits[1];
Bits[0] = measure Qubits[0];
Bits[1] = measure Qubits[1];
