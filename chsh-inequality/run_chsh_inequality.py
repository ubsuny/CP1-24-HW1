# Imports necessary libraries for qisket/ibm functionality
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer, AerSimulator
from qiskit import IBMQ
from qiskit.execute_function import execute
from qiskit.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy
from qiskit_ibm_provider import IBMProvider

# Imports required for data export and plotting
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

# define some default measurement angles (a, a', b, b')
angles = {
    'a': 0,
    'a_prime': np.pi / 4,
    'b': np.pi / 8,
    'b_prime': -np.pi / 8
}

# Function to read the API token from a file
def load_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        api_key = file.readline().strip()
    return api_key

# Set up the quantum circuit to create a Bell state
def create_bell_state():
    qc = QuantumCircuit(2, 2)
    qc.h(0)  # Hadamard gate on the first qubit
    qc.cx(0, 1)  # CNOT gate entangling qubit 0 with qubit 1
    return qc

# Function to save results to a JSON file
def save_results_to_json(result_data, directory="experiment-results"):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Define the filename dynamically
    json_filename = f"chsh-output-{current_time}.json"
    json_filepath = os.path.join(directory, json_filename)

    # Write the result data to a JSON file
    with open(json_filepath, 'w') as json_file:
        json.dump(result_data, json_file, indent=4)

    print(f"Results saved to {json_filepath}")

# Function to plot the results and save as an image
def plot_results(result_data, directory="experiment-results"):
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Define the filename dynamically for the plot
    plot_filename = f"chsh-output-{current_time}.png"
    plot_filepath = os.path.join(directory, plot_filename)

    # Prepare the data for plotting
    labels, counts = zip(*result_data.items())

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color='blue')
    plt.xlabel('Measurement Outcomes')
    plt.ylabel('Counts')
    plt.title('CHSH Inequality Results')

    # Save the plot
    plt.savefig(plot_filepath)
    print(f"Plot saved to {plot_filepath}")
    plt.show()


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

# Analyze the actual output values
def analyze_results(counts):
    results = (counts.get('00', 0) + counts.get('11', 0) -
                   counts.get('01', 0) - counts.get('10', 0)) / shots
    return results


# Main execution: Run on the real quantum device
def run_on_real_device():
    qc = chsh_circuit(angles['a'], angles['b'])

    # Load the API key from the environment variable
    api_key = os.getenv('IBM_QUANTUM_API_KEY')
    # Check if the API key was loaded properly
    if api_key is None:
        raise ValueError("API key not found in environment variables. Please set the IBM_QUANTUM_API_KEY.")

# Load the IBM Quantum account directly using the API key

    # Save and load the account using the API key
    IBMProvider.save_account(api_key, overwrite=True)
    provider = IBMProvider(token=api_key)

    # Get least busy backend from IBMQ
    # Get all available backends
    backends = provider.backends(filters=lambda b: b.configuration().n_qubits >= 2 and not b.configuration().simulator)
    print(f"All Backends: {backends}")
    backend = least_busy(backends)
    print(f"Running on backend: {backend}")

    # create the job and execute it
    simulator = AerSimulator()
    job = execute(qc, backend=simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print(counts)

    # Execute the quantum circuit on the real quantum computer
    # job = execute(qc, backend=backend, shots=1024)
    # result = job.result()
    # counts = result.get_counts()

    # Save result data to JSON
    save_results_to_json(counts)

    # Plot and save the result data
    plot_results(counts)
    # Display result
    plot_histogram(counts).show()

if __name__ == "__main__":
    # First, calculate CHSH parameter S
    S_value = calculate_chsh()
    print(f"CHSH S value: {S_value}")

    # Make sure it doesnt silently fail
    # If the S_value violates the classical limit (2), you can confirm a quantum violation
    if S_value > 2:
        print(f"Violation of CHSH inequality! (S = {S_value})")

    # Run the test on a real quantum device
    run_on_real_device()
