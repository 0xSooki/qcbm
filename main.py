import qcbm.circuit as circ
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import EfficientSU2

arr = np.array([[0, 1, 0, 0, 0], [0, 1, 1, 0, 1], [1, 1, 1, 1, 1]])
n = 5

pairs = circ.get_entangled_pairs(arr)
qc = EfficientSU2(n, entanglement=pairs, reps=5, flatten=True)
print(qc)
