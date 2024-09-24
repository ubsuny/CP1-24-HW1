"""
Module Specifications - quantuncode.py

This module implements the CHSH Inquality via IBM's quantum computing infrastructure.

It is intended to be executed as an application. Functionality includes preparing
a 2-qubit quantum circuit via qiskit, implementing the CHSH inequality, and running
it on the IBM quantum infrastructure via API.

All code sourced from https://learning.quantum.ibm.com/tutorial/chsh-inequality
"""

#TODO: Add exception handling.

#TODO: Consider parameterization for customized execution.

#TODO: Add output handling. Data should be saved as files or handed off to another
#       module for posterity and future analysis.

#TODO: Add a naming scheme for files being saved so that new ones will not overwrite
#       old files with the same name.

#TODO: Consider placing the main routine in a function for greater control over execution


#FIX: QuantumCircuit referenced but never defined
chsh_circuit = QuantumCircuit(2)    # Initialize a quantum circut with 2 qubits
chsh_circuit.h(0)                   # Add a hadamard gate to the first qubit
chsh_circuit.cx(0, 1)               # Add controlled-NOT gate to both qubits


# Define the parameter theta
theta = Parameter("$\\theta$")
# Adds RY gate with theta representing rotation of the qubit's state around the Y-axis
chsh_circuit.ry(theta, 0)

# Render a visual representation of the active circuit.
# Documentation (including parameters details) can be found
# at: https://docs.quantum.ibm.com/guides/visualize-circuits
chsh_circuit.draw(output="mpl", idle_wires=False, style="iqp")

# Designate the total number of phases we are interested in
number_of_phases = 21

# Arrange the phases into a numpy array
phases = np.linspace(0, 2 * np.pi, number_of_phases)

#FIX: This object is created, but never referenced.
# "Phases need to be expressed as list of lists in order to work":
# https://learning.quantum.ibm.com/tutorial/chsh-inequality#create-a-list-of-phase-values-to-be-assigned-later
# There are other ways to handle this issue if clarity becomes a problem
individual_phases = [[ph] for ph in phases]

#FIX:   SparsePauliOp is referenced, but never defined.

# Create a quantum observable using the SparsePauliOp class.
# docs: https://docs.quantum.ibm.com/api/qiskit/qiskit.quantum_info.SparsePauliOp
# <CHSH1> = <AB> - <Ab> + <aB> + <ab> -> <ZZ> - <ZX> + <XZ> + <XX>
observable1 = SparsePauliOp.from_list([("ZZ", 1), ("ZX", -1), ("XZ", 1), ("XX", 1)])

# Create a second quantum observable using the SparsePauliOp class.
# <CHSH2> = <AB> + <Ab> - <aB> + <ab> -> <ZZ> + <ZX> - <XZ> + <XX>
observable2 = SparsePauliOp.from_list([("ZZ", 1), ("ZX", 1), ("XZ", -1), ("XX", 1)])


# Import the qiskit pass manager and prepare a
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Designate a target backend
target = backend.target
# Generate the pass manager
pm = generate_preset_pass_manager(target=target, optimization_level=3)

# Run the circuit on the quantum backend
chsh_isa_circuit = pm.run(chsh_circuit)
# Use qiskit to visually render the circuit output
chsh_isa_circuit.draw(output="mpl", idle_wires=False, style="iqp")

# Apply the actual layout from the circuit to the observable objects
# docs: https://docs.quantum.ibm.com/api/qiskit/qiskit.transpiler.passes.ApplyLayout
isa_observable1 = observable1.apply_layout(layout=chsh_isa_circuit.layout)
isa_observable2 = observable2.apply_layout(layout=chsh_isa_circuit.layout)

#TODO: File output, data retention, or further analysis should happen here.
