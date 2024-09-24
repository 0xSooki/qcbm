from qiskit import QuantumCircuit
from chow_liu_tree import get_tree_representation


def create_circ(n, samples):
    qc = QuantumCircuit(n)
    add_entangling_layer(qc, get_tree_representation(samples))


def add_entangling_layer(qc, tree):
    for pair in tree:
        qc.cx(qc.qubits[pair[0]], qc.qubits[pair[1]])
    print(qc.data)
