import qiskit, qiskit.qasm3
import numpy as np

qc = qiskit.QuantumCircuit(5)
for i in range(5):
    qc.h(i)
    qc.rx(np.pi/4,i)
qc.barrier()
qc.t(4)
qc.p(np.pi/3, 3)
qc.ry(np.pi/2, 2)
qc.ry(np.pi/2, 1)
qc.barrier()
for i in range(4):
    qc.cz(i, i+1)

qc.barrier()
qc.measure_all()

qiskit.qasm3.dumps(qc)

with open("example.qasm", "w") as f:
    f.write(qiskit.qasm3.dumps(qc))

qc.draw('mpl', style='iqx', filename='example_circuit.png')