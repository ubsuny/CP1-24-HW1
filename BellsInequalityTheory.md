# Bell's Inequality

## History

In 1935, Albert Einstein teamed up with Boris Podolsky and Nathan Rosen to publish a paper commonly known by the initials EPR [1](https://cds.cern.ch/record/405662/files/PhysRev.47.777.pdf). Einstein believed that quantum mechanics was an incomplete description of reality.
They argued that Quantum Mechanics (QM) was incomplete because it relied on so-called "Hidden Variables" that could account for some of the uncertainties in QM. Hidden Variables refer to microscopic characteristics of fundamental particles that we cannot currently observe due to technological limitations, although future advancements might change this. 
In other words, we may need more advanced tools to uncover the details at the smallest scales. Since we cannot currently see these variables, they remain "hidden."
However, understanding them could clarify the otherwise puzzling behaviour of particles. 
The Heisenberg Uncertainty Principle (HUP), a fundamental aspect of Quantum Mechanics, posits that these variables not only elude observation but do not exist outside the context of an observation, challenging our conventional understanding of reality.
EPR provided a clear yet impactful definition of what they termed an "element of reality": if a property of a system can be predicted with complete certainty (100%) without influencing that system, then it must relate to an element of reality. This definition is straightforward and widely accepted. We will use it in our proof of Bell's Theorem.
EPR argued that either Hidden Variables exist, or the attributes of particles (such as position, velocity, energy, and polarization) are not real or defined until they are measured. 
This idea aligns with the Heisenberg Uncertainty Principle (HUP). They also claimed that it is "unreasonable" to think that these attributes require observation to be real, thus inferring that Hidden Variables must exist. 
Einstein famously stated, "I think that a particle must have a separate reality independent of the measurements. 
That is: an electron has spin, location, and so on, even when it is not being measured. I like to think that the moon is there even if I am not looking at it." While some accepted this view, others, including Bell, disagreed.
Quantum Mechanics suggests that observation influences reality, and can do so retroactively, a notion that, while strange, is consistent with the evidence. Building on this, Bell demonstrated that local Hidden Variables would lead to contradictions with QM predictions in specific scenarios. Thus, Bell's Theorem builds on EPR, revealing a critical requirement known as Bell's Inequality, which was not immediately apparent until 30 years later.

## Background of Einstein, Podolsky, and Rosen Paradox

On May 15th 1935 Albert Einstein published the paper "Can Quantum-Mechanical Description of Physical 
Reality Be Considered Complete?" alongside his associates Boris Podolsky, and Nathan Rosen.

Einstein, Podolsky, and Rosen begin this paper by plainly explaining a paradox in Quantum Mechanics as follows:

> "In a complete theory there is an element corresponding to each element of reality. A sufficient condition for the reality of a physical quantity is the possibility of predicting it with certainty, without disturbing the system. In quantum mechanics in the case of two physical quantities described by non-commuting operators, the knowledge of one precludes the knowledge of the other. Then either (1) the description of reality given by the wave function in quantum mechanics is not complete or (2) these two quantities cannot have simultaneous reality. Consideration of the problem of making predictions concerning a system on the basis of measurements made on another system that had previously interacted with it leads to the result that if (1) is false then (2) is also false. One is thus led to conclude that the description of reality as given by a wave function is not complete."

*Einstein, A., et al. “Can quantum-mechanical description of physical reality be considered complete?” Physical Review, vol. 47, no. 10, 15 May 1935, pp. 777–780, https://doi.org/10.1103/physrev.47.777.*

To understand what they meant we must first understand as best as we can a few fundamental ideas in quantum mechanics and the founding issues Einstein and his collegues had with them. In Quantum Mechanics a quantum mechanical object, let's refer to it as a particle, can be described probabilistically by a wave function. This means that any observable measurment of said particle is only finite and measurable after a measurment has been taken. Before that measurement the particle has a probability of being any number of possible outcomes defined by a function. Afterward the wave function would "collapse" into a single value.

Werner Heisenberg would later go on to theorize that after the first mesurment was mad and the value defined, if a second measurement were made and defined the first measurment were retaken, then the supposedly fixed first value could be measured differently. The first value is "reset" back to the probabilistic wave function. This meant that measurments themselves were uncertain if further measurments of different factors are taken. This is refered to as the Heisenberg Unertainty Principle.

Similarly Erwin Schrödinger had a famous though experiment where he posited that a cat in a contained box that could not be looked into and a radioactive souce connected to a hammer over a sealed vial of poison would randomly be broken by the hammer killing the cat. This meant that while the box was unopened no outside observer could know whether the cat was alive or dead and therefore until the box is opened and a definite measurment taken the cat is both alive and dead. Both states held in what he called "superposition". Because of the feline subject, this thought experiment is refered to as "Schrödinger's Cat".

Einstein, Podolsky, and Rosen perform a similar thought experiment. A pair of quantum particles are taken from the same source and are linked or "entangled". This means that when a measurment of the same observable is performed on both particles the value is always the same even if the value is "reset" using the Heisenberg Uncertainty Principle. This also means that a measurement of one particle will always tell us the measurment of the other, even before a measurment on particle 2 can be performed. Einstein, Podolsky, and Rosen had to major problems with this as well as Quantum Mechanics. Einstein believed that...

> "Any serious consideration of a physical theory must take into account the distinction between the objective reality, which is independent of any theory, and the physical concepts with which the theory operates. These concepts are intended to correspond with the objective reality, and by means of these concepts we picture this reality to ourselves."

*Einstein, A., et al. “Can quantum-mechanical description of physical reality be considered complete?” Physical Review, vol. 47, no. 10, 15 May 1935, pp. 777–780, https://doi.org/10.1103/physrev.47.777.*

This was a widely held belief that objects in nature are strictly predefined whether or not there is an observer or a theory to define them. Popularly that if a tree falls in the forest and no one is around to hear it, it still makes a sound. Einstein felt the inditerminite nature of quantum mechanical theory ran opposite to this. He along with Podolsky and Rosen also believed that if there were no predefined property of of a quantum system then entaglement was incombatible with Einstein's theory of relativity. This is what they outline in their paper. Since there is no maximum distance two entangled particles can be from each other and still be entangled hen they shouldn't be able to send information instantaniously to each other. Say we have two entangled particles. One on the Earth and one on the Moon and they both attatched to measurement devices. Then a scientist here on Earth measures the first entangled particle and one nanosecond later the other scientitst on the moon measures the second particle. Both measurments are identicle because the pair is entangled. Einstein says this is impossible because the first particle must inform the second what it has been measured as so they can be identical, but for that to be true the information would have to travel faster than the speed of light to beat the one nanosecond later measurement the second scientist makes. This breaks the thory of relativity that nothing can travel faster than the speed of light. So Einstein, Podolsky, and Rosen believe that either there is a secret property that is not described in Quantum Mechanis or the two particles are not simultaneously entangled. This is the paradox as laid out in the paper. This conclusion would stand unchallenged until John Stewart Bell would publish a paper contradicting the EPR paradox in 1964.


Background information edited from:

David J. Griffiths, Gale Dick; Introduction to Quantum Mechanics. Physics Today 1 September 1995; 48 (9): 94. https://doi.org/10.1063/1.2808172

## Physics of EPR

Assumptions in their argument [EPR Article]:
- locality – no influence between space-like separated events.
- realism – properties of objects exist in some sense independent of measurement choice.
- free will of experimenter
- we can choose what we measure independently of the state we are measuring. 

In particular they favor a local, deterministic theory. Theories of this type belong to a class called local hidden variable theories.

What are hidden variable theories?
- The behavior of the states in the theory are not only governed by measurable degrees of freedom but have additional ‘hidden’ degrees of freedom that complete the description of their behavior.
- ‘Hidden’ because if states with prescribed values of these variables can be prepared or manipulated then predictions of the theory would be in contradiction with experiments.

As applied to quantum mechanics: 
- Wave function or state vector not a complete description of the physical state of a system. 
- Complete description would also include the specification of the hidden variables 
   describing that state
- If one could prepare quantum states with prescribed values of that hidden variable or manipulate them at will, quantum mechanical predictions would disagree with experiments. 

In the early 1950's David Bohm was a young Physics professor at Princeton University. Einstein was at Princeton at this time. Bohm spent many years in search of hidden variables, unobserved factors inside, say, a radioactive atom that determines when it is going to decay. In a hidden variable theory, the time for the decay to occur is not random, although the variable controlling the process is hidden from us. In 1952 Bohm constructs a hidden variable theory that reproduces quantum mechanics – de Broglie-Bohm mechanics. Bohm’s model is not of the desire of EPR who want a local, hidden variable theory. [2]

The debate about the completeness of quantum mechanics was considered to be merely philosophical until 1964 when John Bell showed that quantum mechanics and hidden-variable theories were mathematically incompatible. He derived an inequality based on Bohm-type quantum systems which showed that any local realistic theory and quantum mechanics predicted two different probabilistic outcomes. His work was further elaborated on by Clauser, Horne, Shimony and Holt.

Bell theorem.
It was cast in terms of a hidden variable theory.The essence of Bell’s theorem is that quantum mechanical probabilities cannot arise from the ignorance of local pre-existing variables. In other words, if we want to assign pre-existing (but hidden) properties to explain probabilities in quantum measurements, these properties must be nonlocal. Bell takes EPRs argument as a working hypothesis, that a local hidden variable theory exists, reproducing the results of Quantum Mechanics and tries to derive experimental consequences.
The theorem's assumes that:
- no influence between space-like separated like separated events.
- properties of objects exist in some sense
- independent of measurement choice.

## EPR and Quantum Mechanics

As discussed above, EPR claimed that there was a sufficient condition for a physical property to be an element of reality, namely, that it be possible to predict with certainty the value that property will have, immediately before measurement. The idea was that any complete physical theory must have such elements of reality represented in it. As per EPR, quantum mechanics would be incomplete. However, experimental evidence led to the fall of that point of view, while agreeing with quantum mechanics. A key aspect for reaching those experiments is the thought experiment of Bell's inequality.

We discuss a specific one out of the set of results known as Bell's inequality, namely the CHSH inequality. Consider the following experiment [3], Charlie prepares two particles out of which he sends one particle to Alice, and the second particle to Bob. We are agnostic to the method of preparation used by Charlie. 

Once Alice receives her particle, she performs a measurement on it. Considering that she has available two different measurement apparatuses, corresponding to two different measurements. These measurements are of physical properties say, $P_Q$ and $P_R$, respectively. Alice uses a random method to decide which measurement to perform and the measurements can each have one of two outcomes, +1 or −1. Suppose Alice’s particle has a value $Q$ for the property $P_Q$. $Q$ is assumed to be an objective property of Alice’s particle, simply revealed by the measurement. And similaarly, for the measurement of the property $R$.

Similarly, we suppose that Bob is capable of measuring one of two properties, $P_S$ or $P_T$ ,each taking value +1 or −1. Bob also does not decide beforehand which property he will measure, but waits until he has received the particle and then chooses randomly. The experiment is arranged so that Alice and Bob's measurements are simultaneous/causally disconnected. Therefore, one measurement cannot disturb the result of other.

It is easy to see that the quantity $QS + RS + RT − QT = (Q+R)S + (R−Q)T$, can only assume two values,

$$QS + RS + RT − QT = (Q+R)S + (R−Q)T = \pm 2$$

Which in turn gives the Bell's inequality (on the expectation value of QS + RS + RT − QT),

$$\langle QS + RS + RT − QT\rangle = \langle QS \rangle + \langle RS \rangle + \langle RT \rangle - \langle QT \rangle \leq 2$$

For details one may read through [3].

If we now consider this experiment with manifestly quantum particles, i.e. if Charlie prepares the quantum system of two qubits in the state, 

$$ \ket{\Psi} = \frac{1}{\sqrt{2}} \left( |01\rangle - |10\rangle \right) $$

The spin singlet state, and Alice and Bob perform the following measurements:

$$Q = Z_1, R = X_1$$

$$S = \frac{-Z_2 - X_2}{\sqrt{2}}, T = \frac{Z_2 - X_2}{\sqrt{2}} $$

We get for the Bell's inequality equation,

$$\langle QS \rangle + \langle RS \rangle + \langle RT \rangle - \langle QT \rangle = 2\sqrt{2}$$

Thus, quantum mechnaics manifestly violates Bell's inequalities. Turns out, through a number of experiments, this is indeed the case and thus the EPR assumptions were invalid. One of the interesting inferences out of this is that entanglement is inherently quantum mechanical in nature [3, 4].

## Experiments in Bell's Inequality

Experimental set-ups testing Bell's inequality may involve a two channel set-up or a single-channel set-up. 
### Two Channel Scheme
![Alt Text](https://encyclopedia.pub/media/common/202211/mceclip0-63808cdc4873a.png)

The source S produces pairs of photons sent in opposite directions where they encounter two-channel polarisers. The orientations of the polarizers are set b the experimenter. The coincidence monitor (CM) dectects coincidences and counts them. Coincidences are simultaneous detections recorded as $$'++','+-','-+','--'$$. The angles which the polarizers are set to, $$a, a', b, b'$$ are generally chosen to be $$0, 45, 22.5, and 67.5$$ degrees respectively. These are the "Bell Test Angles," which are chosen for giving the greatest violation of Bell's inequality with the quantum mechanical formula. With this, the states used in Bell's inequality are $$<ab>, <ab'>, <a'b>, <a'b'>$$ The experimental esitmate of each state E(a,b) is calculated from the coincidences. 

$$E=(N<sub>++</sub>+N<sub>--</sub>-N<sub>+-</sub>-N<sub>-+</sub>)/(N<sub>++</sub>+N<sub>--</sub>+N<sub>+-</sub>+N<sub>-+</sub>)$$. 

Once E has been estimated for all four states the test statistic may be calculated as 

$$S=E(a,b)-E(a,b')+E(a',b)+E(a',b')$$ If this is numerically greater than 2, it has infringed the CHSH inequality. 

### Single Channel Scheme
![Alt Text](https://encyclopedia.pub/media/common/202211/mceclip1-63808d1238b46.png)

A source S produces pairs of photons sent in opposite directions to encounter a single channel polarizer with an orientation set by the experimenter. Again, coincidences are counted by the Coincidence Monitor. What sets this apart from the two-channel scheme is that there are additional subexperiments to get states where one or both polarizers are absent. This set-up was used prior to 1982, described in Clauser, Horne, Shimony, and Holt in their 1969 article. 
This time, the test statistic is defined by 

$$S=(E(a,b)-E(a,b')+E(a',b)+E(a',b')-E(a',\infty )-E(\infty ,b))/N(\infty ,\infty )$$

Where \infty indicates the absence of a polarizer. If S exceeds zero, then the experiment is said to have infringed Bell's inequaltiy. In order to derive the above equation in the 1969 paper by CHSH, they made an extra assumption referred to as "fair sampling." This refers to the probablity of detection of a given photon once it has passed the polarizer is independent of the polarizer setting. 

There have also been more recent experiments performed such that they were not subject to the locality or detection loophole. An experiment free of the locality loophole ensures that a new setting is chosen before the signals may commnunicate the setting from one wing of the experiment to the other. To bypass the detection loophole, 100% of the successful measurement outcomes in one wing of the experiment must be paired with a successful measurement in the other wing. This percentage is referred to as the efficiency of the experiment. 

Some of the best known and more recent experiments include: 

### Freedman and Clauser (1972)
This was the first actual Bell test. It used Freedman's inequality

### Aspect et al. (1982)
Alain Aspect and his team conducted three bell tests using calcium cascade sources. The first and last used the CH74 inequality while the seccond was the first application of the CHSH inequality. The third test is most famous for the fact that the choice between the two settings on each side was made during the flight of the photons as originally suggested by John Bell

### Weihs et al. (1998): Experiment under "Strict Einstein Locality" Conditions
Gregor Weihs and a team conducted an experiment to close the locality loophole. The choice of detector was made using a quantum process to ensure that it was random. 

### Rowe et al. (2001): the First to Close the Detection Loophole
This experiment by the group of David Wineland used two entangled trapped ions to get detection efficiencies well over 90%.

## References
[1] Albert Einstein, Boris Podolsky, and Nathan Rosen. “Can quantum-mechanical description of physical reality be considered complete?” In: Physical review 47.10 (1935), p. 777.

[2] D. Bohm, A suggested interpretation of the quantum theory in terms of hidden variables. Phys. Rev. 85, 166 (1952)

[3] Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information: 10th Anniversary Edition. Cambridge: Cambridge University Press.

[4] Stephen Barnett. 2009. Quantum Information. Oxford University Press, Inc., USA.

[5] “Bell Test Experiments.” Encyclopedia, HandWiki, 29 Nov. 2022, encyclopedia.pub/entry/36569. 
