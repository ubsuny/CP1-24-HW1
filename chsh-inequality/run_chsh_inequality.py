# Import necessary libraries
import numpy as np
from qiskit import QuantumCircuit, Aer, IBMQ
from qiskit.execute_function import execute
from qiskit.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy


# Initialize IBMQ account
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')

# Set up the quantum circuit to create a Bell state
def create_bell_state():
    qc = QuantumCircuit(2, 2)
    qc.h(0)  # Hadamard gate on the first qubit
    qc.cx(0, 1)  # CNOT gate entangling qubit 0 with qubit 1
    return qc

# Define measurement angles (a, a', b, b')
angles = {
    'a': 0,
    'a_prime': np.pi / 4,
    'b': np.pi / 8,
    'b_prime': -np.pi / 8
}

# Create the CHSH inequality circuit
def chsh_circuit(angle_a, angle_b):
    qc = create_bell_state()

    # Rotate qubit 0 by angle_a
    qc.ry(2 * angle_a, 0)

    # Rotate qubit 1 by angle_b
    qc.ry(2 * angle_b, 1)

    # Measure both qubits
    qc.measure([0, 1], [0, 1])

    return qc

# Simulate and get expectation values
def simulate_chsh(angle_a, angle_b, shots=1024):
    qc = chsh_circuit(angle_a, angle_b)
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=shots).result()
    counts = result.get_counts()

    # Calculate expectation value based on results
    expectation = (counts.get('00', 0) + counts.get('11', 0) -
                   counts.get('01', 0) - counts.get('10', 0)) / shots
    return expectation

# Calculate the S parameter for CHSH
def calculate_chsh():
    E_ab = simulate_chsh(angles['a'], angles['b'])
    E_ab_prime = simulate_chsh(angles['a'], angles['b_prime'])
    E_a_prime_b = simulate_chsh(angles['a_prime'], angles['b'])
    E_a_prime_b_prime = simulate_chsh(angles['a_prime'], angles['b_prime'])

    S = E_ab + E_ab_prime + E_a_prime_b - E_a_prime_b_prime
    return S

# Main execution: Run on the real quantum device
def run_on_real_device():
    qc = chsh_circuit(angles['a'], angles['b'])

    # Get least busy backend from IBMQ
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 2 and not x.configuration().simulator))

    # Execute the quantum circuit on the real quantum computer
    job = execute(qc, backend=backend, shots=1024)
    result = job.result()
    counts = result.get_counts()

    # Display result
    plot_histogram(counts).show()

if __name__ == "__main__":
    # First, calculate CHSH parameter S
    S_value = calculate_chsh()
    print(f"CHSH S value: {S_value}")

    # If the S_value violates the classical limit (2), you can confirm a quantum violation
    if S_value > 2:
        print(f"Violation of CHSH inequality! (S = {S_value})")

    # Run the test on a real quantum device
    run_on_real_device()
