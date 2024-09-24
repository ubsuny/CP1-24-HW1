# Bell Inequality

## History
-Einstein believed that quantum mechanics was an incomplete description of reality. [1](https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777). Einstein, in particular believed that quantum mechanics was an approximation to a local, deterministic theory. 
-	Story starts with a famous paper by Einstein, Podolsky and Rosen in 1935.In the title of their 1935 article, Einstein, Podolsky and Rosen [EPR] ask whether quantum mechanics can be considered as a complete description of physical reality. [1](https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777)

## Assumptions in their argument [EPR Article]:
- locality – no influence between space-like separated events.
- realism – properties of objects exist in some sense independent of measurement choice.
- free will of experimenter
- we can choose what we measure independently of the state we are measuring. 

In particular they favor a local, deterministic theory. Theories of this type belong to a class called local hidden variable theories.

## What are hidden variable theories?
- The behavior of the states in the theory are not only governed by measurable degrees of freedom but have additional ‘hidden’ degrees of freedom that complete the description of their behavior.
- ‘Hidden’ because if states with prescribed values of these variables can be prepared or manipulated then predictions of the theory would be in contradiction with experiments.

As applied to quantum mechanics: 
- Wave function or state vector not a complete description of the physical state of a system. 
- Complete description would also include the specification of the hidden variables 
   describing that state
- If one could prepare quantum states with prescribed values of that hidden variable or manipulate them at will, quantum mechanical predictions would disagree with experiments. 


In the early 1950's David Bohm was a young Physics professor at Princeton University. Einstein was at Princeton at this time. Bohm spent many years in search of hidden variables, unobserved factors inside, say, a radioactive atom that determines when it is going to decay. In a hidden variable theory, the time for the decay to occur is not random, although the variable controlling the process is hidden from us. In 1952 Bohm constructs a hidden variable theory that reproduces quantum mechanics – de Broglie-Bohm mechanics. Bohm’s model is not of the desire of EPR who want a local, hidden variable theory. [2](https://journals.aps.org/pr/abstract/10.1103/PhysRev.85.166)

The debate about the completeness of quantum mechanics was considered to be merely philosophical until 1964 when John Bell showed that quantum mechanics and hidden-variable theories were mathematically incompatible. He derived an inequality based on Bohm-type quantum systems which showed that any local realistic theory and quantum mechanics predicted two different probabilistic outcomes. His work was further elaborated on by Clauser, Horne, Shimony and Holt.

## Bell theorem.
It was cast in terms of a hidden variable theory.The essence of Bell’s theorem is that quantum mechanical probabilities cannot arise from the ignorance of local pre-existing variables. In other words, if we want to assign pre-existing (but hidden) properties to explain probabilities in quantum measurements, these properties must be nonlocal. Bell takes EPRs argument as a working hypothesis, that a local hidden variable theory exists, reproducing the results of Quantum Mechanics and tries to derive experimental consequences.
The theorem's assumes that:
- no influence between space-like separated like separated events (locality).
- properties of objects exist in some sense (realism)
- independent of measurement choice (free will of experimenter)

## Bell’s inequalities – The CHSH*[3](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.23.880) inequality

![image](https://github.com/user-attachments/assets/cfdac3d2-eaf6-4f41-8e44-0c1ad0ed2220)

- Perform experiment N times, each trial labelled by n.
- Two measurement settings on each particle represented by vectors *a, a’* and *b, b’*
- Measurement outcomes labelled $$\displaystyle{a}_{{n}},{a}_{{n}}\text{'}{\quad\text{and}\quad}{b}_{{n}},{b}_{{n}}\text{'}$$.
- There can be two measurement outcomes with value 1 or -1
- Assume each measurement reveals a pre-existing property (realism)
- Assume measurement outcome on one of particles not influenced by measurement
setting on the other particle (locality)
- Assume measurement setting chosen independent of state of particles (free will)

Consider the quantity $\displaystyle{{g}_{{n}}}$, a combination of the measurement outcomes on the $\displaystyle{n}^{{{t}{h}}}$ trial:

$\displaystyle{{g}_{{n}}=}{a}_{{n}}{b}_{{n}}+{a}_{{n}}{{b}_{{n}}^{'}}+{{a}_{{n}}^{'}}{b}_{{n}}-{{a}_{{n}}^{'}}{b}^{'}$

$\displaystyle{{g}_{{n}}=}{a}_{{n}}{\left({b}_{{n}}+{{b}_{{n}}^{'}}\right)}+{{a}_{{n}}^{'}}{\left({b}_{{n}}-{{b}_{{n}}^{'}}\right)}$

$\displaystyle{{g}_{{{n}}}=}\pm{2}$

The expectation value is therefore:

$\displaystyle{\left|\lim_{{{N}\to\infty}}\frac{1}{{N}}{\sum_{{{n}={1}}}^{{N}}}{{g}_{{n}}{\left|=\right|}}{C}{\left({a},{b}\right)}+{C}{\left({a},{b}^{'}\right)}+{C}{\left({a}^{'},{b}\right)}-{C}{\left({a}^{'},{b}^{'}\right)}\right|}\le{2}$

$\displaystyle{C}{\left({a},{b}\right)}={|}\lim_{{{N}\to\infty}}\frac{1}{{N}}{\sum_{{{n}={1}}}^{{N}}}{a}_{{n}}{b}_{{n}}$

$\displaystyle{\left|{C}{\left({a},{b}\right)}+{C}{\left({a},{b}^{'}\right)}+{C}{\left({a}^{'},{b}\right)}-{C}{\left({a}^{'},{b}^{'}\right)}\right|}\le{2}$

Note: Note that in deriving the CHSH inequality we have not assumed any particular theory, only that it has to be a local, realistic theory. This is the power, generality and simplicity of the result. It provides a bound on any theory of this type.



References:

[1](https://journals.aps.org/pr/abstract/10.1103/PhysRev.47.777) Albert Einstein, Boris Podolsky, and Nathan Rosen. “Can quantum-mechanical description of physical reality be considered complete?” In: Physical review 47.10 (1935), p. 777.

[2](https://journals.aps.org/pr/abstract/10.1103/PhysRev.85.166) D. Bohm, A suggested interpretation of the quantum theory in terms of hidden variables. Phys. Rev. 85, 166 (1952)

[3](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.23.880) J. F. Clauser, M. A. Horne, A. Shimony and R. A. Holt. Proposed experiment to
test local hidden-variable theories. Phys. Rev. Lett. 23, 880 (1969)
