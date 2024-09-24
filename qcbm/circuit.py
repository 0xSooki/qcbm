from qiskit import QuantumCircuit
from qcbm.chow_liu_tree import get_tree_representation
from qiskit.circuit.library import EfficientSU2


def create_circ(n, samples):
    qc = QuantumCircuit(n)
    add_entangling_layer(qc, get_tree_representation(samples))


def create_qcbm(n, samples):
    pairs = [[pair[0], pair[1]] for pair in get_tree_representation(samples)]
    print(len(pairs))
    circuit = EfficientSU2(n, entanglement=pairs, reps=1)
    return circuit


def add_entangling_layer(qc, tree):
    for pair in tree:
        qc.cx(qc.qubits[pair[0]], qc.qubits[pair[1]])
