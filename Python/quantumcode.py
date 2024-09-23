#Comments for a line are done above said line
#I copied this from https://learning.quantum.ibm.com/tutorial/chsh-inequality
#Defining the circuit with the parameter theta
theta = Parameter("$\\theta$")

#This initializes the quantum circut 'same link as above'
chsh_circuit = QuantumCircuit(2)
#Adds the hadamard gate 'same link as above'
chsh_circuit.h(0)
#Adds the controlled-NOT gate 'same link as above'
chsh_circuit.cx(0, 1)
#Adds the RY gate with the theta representing the rotation of the qubit state around an axis y 'same link as above'
chsh_circuit.ry(theta, 0)
#The func chsh_circuit.draw creates and outputs a picture that shows the quantum circut in the way you would learn about them i.e. the way IBM quantum learning lets you work on them
chsh_circuit.draw(output="mpl", idle_wires=False, style="iqp")


#Now to continue onto creating a list of phase values to be used latter copied from same link from line 2

number_of_phases = 21
phases = np.linspace(0, 2 * np.pi, number_of_phases)
# 'Phases need to be expressed as list of lists in order to work' also copied for your convieneance
individual_phases = [[ph] for ph in phases]


# <CHSH1> = <AB> - <Ab> + <aB> + <ab> -> <ZZ> - <ZX> + <XZ> + <XX>
observable1 = SparsePauliOp.from_list([("ZZ", 1), ("ZX", -1), ("XZ", 1), ("XX", 1)])

# <CHSH2> = <AB> + <Ab> - <aB> + <ab> -> <ZZ> + <ZX> - <XZ> + <XX>
observable2 = SparsePauliOp.from_list([("ZZ", 1), ("ZX", 1), ("XZ", -1), ("XX", 1)])


from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

target = backend.target
pm = generate_preset_pass_manager(target=target, optimization_level=3)

chsh_isa_circuit = pm.run(chsh_circuit)
chsh_isa_circuit.draw(output="mpl", idle_wires=False, style="iqp")


isa_observable1 = observable1.apply_layout(layout=chsh_isa_circuit.layout)
isa_observable2 = observable2.apply_layout(layout=chsh_isa_circuit.layout)
