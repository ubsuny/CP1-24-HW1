# Bell's Inequality Documentation

## Introduction
Bell's inequality is a crucial test in quantum mechanics that distinguishes between quantum mechanical predictions and classical physics assumptions, particularly local hidden variable theories.

## Key Concepts

-Local Hidden Variable Theories: Assume that the properties of particles are determined by hidden variables and are not influenced by actions at a distance.
-Quantum Entanglement: A phenomenon where two particles remain interconnected, such that the state of one directly affects the state of the other, regardless of the distance between them.

## Mathematical Derivation of Bell's Inequality

To understand Bell's inequality, consider two entangled particles measured by observers Alice and Bob with different settings. The expectation value of their measurements is given by:

$$ E(a, b) = \int d\lambda \, \rho(\lambda) A(a, \lambda) B(b, \lambda) $$

where:
- \( A(a, \lambda) \) and \( B(b, \lambda) \) represent measurement outcomes.
- \( \rho(\lambda) \) is the probability distribution of hidden variables.

 ## Derivation

1. The expectation value of the product of Alice's and Bob's outcomes for a given pair of settings \( (a, b) \) is defined as:

   $$ E(a, b) = \int d\lambda \, \rho(\lambda) A(a, \lambda) B(b, \lambda) $$

2. Combine expectation values to form the inequality:

   $$ S = E(a, b) - E(a, b') + E(a', b) + E(a', b') $$

3. Under local hidden variable assumptions, we derive:

   $$ |S| \leq 2 $$
