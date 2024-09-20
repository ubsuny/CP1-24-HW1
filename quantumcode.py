theta = Parameter("$\\theta$")
# this initializes thequantum circut 'same link
chsh_circuit = QuantumCircuit(2)
#adds the hadamard gate
chsh_circuit.h(0)
chsh_circuit.cx(0, 1)
chsh_circuit.ry(theta, 0)
chsh_circuit.draw(output="mpl", idle_wires=False, style="iqp")

#i copied this from https://learning.quantum.ibm.com/tutorial/chsh-inequality
