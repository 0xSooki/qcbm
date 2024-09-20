from qiskit import QuantumCircuit

def create_circ(n):
    qc = QuantumCircuit(n)
    add_entangling_layer(qc, [[1,2],[0,3]])

def add_entangling_layer(qc, tree):
    for pair in tree:
        qc.cx(qc.qubits[pair[0]], qc.qubits[pair[1]])
    print(qc.data)