from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


def create_circ(n, samples):
    qc = QuantumCircuit(n)
    add_entangling_layer(qc, get_tree_representation(samples))
    qc.measure_all()
    measure_circ(qc,100)

def add_entangling_layer(qc, tree):
    for pair in tree:
        qc.cx(qc.qubits[pair[0]], qc.qubits[pair[1]])
    print(qc.data)
def measure_circ(qc, N):
    sampler = StatevectorSampler(shots=N)
    pm = generate_preset_pass_manager(optimization_level=1)
    result = sampler.run([qc]).result()
    data_pub = result[0].data
    bitstrings = data_pub.meas.get_bitstrings()
    print(f"The number of bitstrings is: {len(bitstrings)}")
    counts = data_pub.meas.get_counts()
    print(f"The counts are: {counts}")
