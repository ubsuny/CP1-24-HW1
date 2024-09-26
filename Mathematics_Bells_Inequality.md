# Bell's Inequality Documentation

## Introduction
Bell's inequality is a crucial test in quantum mechanics that distinguishes between quantum mechanical predictions and classical physics assumptions, particularly local hidden variable theories.

## Key Concepts
- Local Hidden Variable Theories: Assume that the properties of particles are determined by hidden variables and are not influenced by actions at a distance. Local Hidden Variable   theories offer a classical way to explain measurement outcomes by assuming that hidden variables determine the results, respecting locality and realism.
- Quantum Entanglement: A phenomenon where two particles remain interconnected, such that the state of one directly affects the state of the other, regardless of the distance between them. # Quantum Entanglement in the Context of Bell’s Inequality

Consider two quantum particles, often referred to as qubits, in an entangled state. A common example of an entangled state used in Bell’s inequality tests is the **Bell state**, also known as the singlet state:

$$
|\psi\rangle = \frac{1}{\sqrt{2}} (|01\rangle - |10\rangle)
$$

This state describes two qubits, where:
\(|01\rangle\): The first qubit is in state \(|0\rangle\) (e.g., spin down), and the second is in state \(|1\rangle\) (e.g., spin up).
\(|10\rangle\): The first qubit is in state \(|1\rangle\) (spin up), and the second is in state \(|0\rangle\) (spin down).

The overall state is a superposition where the particles are perfectly anti-correlated.

## Mathematical Derivation of Bell's Inequality

To understand Bell's inequality, consider two entangled particles measured by observers Alice and Bob with different settings. The expectation value of their measurements is given by:

$$ E(a, b) = \int d\lambda \, \rho(\lambda) A(a, \lambda) B(b, \lambda) $$

where:
`$A(a, \lambda)$` and `$B(b, \lambda)$` represent measurement outcomes.
`$\rho(\lambda)$` is the probability distribution of hidden variables.

## Derivation

The expectation value of the product of Alice's and Bob's outcomes for a given pair of settings \( (a, b) \) is defined as:
 $$
 E(a, b) = \int d\lambda \, \rho(\lambda) A(a, \lambda) B(b, \lambda)
 $$

Combine expectation values to form the inequality:
$$
S = E(a, b) - E(a, b') + E(a', b) + E(a', b')
$$

Under local hidden variable assumptions, we derive:

$$
|S| \leq 2
$$


### Referances 
1. https://cds.cern.ch/record/111654/files/vol1p195-200_001.pdf
