# Bell Inequality
## History:  
In 1935, Albert Einstein teamed up with Boris Podolsky and Nathan Rosen to publish a paper commonly known by the initials EPR[1](https://cds.cern.ch/record/405662/files/PhysRev.47.777.pdf). 
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



## Hidden Variable Theory:
* Arguement about uncertanity property of Quantum Mechanics
* Hidden Variable
   * Investing Quantum Mechanics with Local Realism
   * Underlying deterministic unknown variable in Quantum Mechanics
* Bohm's Hidden Variable Theory
* Local Hidden Variable Theory
   * Principle that an object is only directly influenced by its immediate surroundings
* EPR paradox - showed non-locality of Quantum Mechanics
   * Two Photons that separated so far apart
   * The measurements od onedetermining the other one's states
* Local Hidden Variable
   *  a quantity whose value is presently unknown with local property
      "Spooky action at a distance" [2] (https://www.quantamagazine.org/how-bells-theorem-proved-spooky-action-at-a-distance-is-real-20210720/)
## Bell's theorem
* Proppsed by John Stewart Bell, in the paper that " On the Einstein- Podolsky-Rosen paradox", 1964.
* A way of distinguishing experimentally between local hidden variable theories and the predictions of Quantum Mechanics
* Bell's Inequality - $\displaystyle\rho{\left({a},{c}\right)}-\rho{\left({b},{a}\right)}-\rho{\left({b},{c}\right)}\le{1}$
   * Inequality that derived from local hidden variable theory
   * Any Quantum correlations under local hidden variable theory do not satisfy bell's inequalities.
   * Demonstration by bell test experiments
* Simple version of a Bell's Inequality
   * Various possible polarization combinations of the two EPR photon [3] (https://www.lesswrong.com/posts/AnHJX42C6r6deohTG/bell-s-theorem-no-epr-reality)

     <img width="319" alt="image" src="https://github.com/user-attachments/assets/9949b0a7-00a4-4c56-a9eb-d60024c5d8dc">

    $\displaystyle{P}{\left({R}_{{1}}\right)}\le{P}{\left({R}_{{2}}\right)}+{P}{\left({R}_{{3}}\right)}$

  The Probability that one photon will pass at $\displaystyle{0}^{o}$ and other will not pass at $\displaystyle{22.5}^{o}$
$\displaystyle+$
  The Probability that one photon will pass at $\displaystyle{22.5}^{o}$ and other will not pass at $\displaystyle{45}^{o}$
$\displaystyle\ge$
  The probability that one photon will pass at $\displaystyle{0}^{o}$ while the other will not pass at $\displaystyle{45}^{o}$


* Quantum Mechanical Calcualtion
   * Photon lineraly polarized at an angle $\displaystyle\theta$ to the horizontal

     $\displaystyle{\left|\psi{\left(\theta\right)}>= \cos{{\left(\theta\right)}}\right|}{H}>+ \sin{{\left(\theta\right)}}{|}{V}>$
   * Probability that such a photon will pass a horizontally-oriented beamsplitter

     $\displaystyle{P}_{{H}}={\left|<{H}\right|}\psi{\left(\theta\right)}>{|}^{2}={{\cos}^{2}\theta}$

   * Two different photon modes: propagating to the left (L) and to the right (R)
   * EPR state with the two orthogonal polarization states ( generalized form : $\displaystyle\theta$ and $\displaystyle\theta+\frac{\pi}{{2}}$ , instead of horizontal and vertical) 
 
  $\displaystyle{|}\psi_{\text{EPR}}>=\frac{1}{\sqrt{{2}}}{\left[{\left|\psi{\left(\theta\right)},{L}>\right|}{\left|\psi{\left(\theta\right)},{R}>+\right|}\psi{\left(\theta+\frac{\pi}{{2}}\right)},{L}>{|}\psi{\left(\theta+\frac{\pi}{{2}}\right)},{R}>\right]}$

   * Consider that examine this state with a horizontal polarizer on the left and a polarizer at an angle $\displaystyle\phi$ to the horizontal on the right, then amplitude is
   $\displaystyle{A}={\left(<{H},{L}{\left|<\psi{\left(\theta\right)},{R}\right|}\right)}{|}\psi_{{{E}{P}{R}}}>$
    $\displaystyle{A}=\frac{1}{\sqrt{{2}}}{\left(<{H},{L}{\left|<\psi{\left(\theta\right)},{L}><\psi{\left(\phi\right)},{R}\right|}\psi{\left(\theta\right)},{R}>+<{H},{L}{\left|<\psi{\left(\theta+\frac{\pi}{{2}}\right)},{L}><\psi{\left(\phi\right)},{R}\right|}\psi{\left(\theta+\frac{\pi}{{2}}\right)},{R}>\right)}$

  Note that we can write
  $\displaystyle<\psi{\left(\phi\right)}{\left|\psi{\left(\theta\right)}>=<{H}\right|}\psi{\left(\theta-\phi\right)}>$

   * Amplitude is independent of the angle $\displaystyle\theta$ of the polarization axs of the EPR
    $\displaystyle{A}=\frac{1}{{\sqrt{{{2}}}}}\cdot{\left[ \cos{\theta}\cdot \cos{{\left(\theta-\phi\right)}}+ \cos{{\left(\theta+\frac{\pi}{{2}}\right)}}\cdot \cos{{\left(\theta+\frac{\pi}{{2}}-\phi\right)}}\right]}$

$\displaystyle={1}\sqrt{{2}}{\left[ \cos{\theta} \cos{{\left(\theta-\phi\right)}}+ \sin{{\left(\theta\right)}} \sin{{\left(\theta-\phi\right)}}\right]};$

$={1}\sqrt{{2}}{1}{2}{\left[ \cos{{\left(\phi\right)}}+ \cos{{\left({2}\theta-\phi\right)}}+ \cos{{\left(\phi\right)}}- \cos{{\left({2}\theta-\phi\right)}}\right]};$

$={1}\sqrt{{2}} \cos{\phi}$

   * We can conclude that the probabilty of the left photon passing the left polarizer at an angle $\displaystyle{0}$ and the right photon passing the right polarizer at an angle $\displaystyle\phi$
      $\displaystyle{P}={\left|{A}\right|}^{2}=\frac{1}{{2}}\cdot{{\cos}^{2}\phi}$
    If a photon on the right passes at an angle $\displaystyle\phi$, then it fails to emerge from the other arm of a polarization beamspitter, an arm that passes a photon of the polarization angle $\displaystyle\phi-\frac{\pi}{{2}}$.
    Probability of the left photon passing the left polarizer at angle $\displaystyle{0}$ and the right photon failing to pass the right polarizer at an angle $\displaystyle\phi$ is
    $\displaystyle{P}_{{\phi}}=\frac{1}{{2}}\cdot{{\cos}^{2}{\left(\phi+\frac{-\pi}{{2}}\right)}}=\frac{1}{{2}}\cdot{{\sin}^{2}\phi}$
The choice of the polarizer orientation on the left as horizontalis arbitrary.

The probability that one photon will pass at $\displaystyle{0}^{o}$ and the other will not pass at $\displaystyle{22.5}^{o}$ 
      $\displaystyle{\left(\frac{1}{{2}}\right)}{{\sin}^{2}{\left({22.5}^{o}\right)}}={0.0732}$
        +
The probability that one photon will pass at $\displaystyle{22.5}^{o}$ and the other will not pass at $\displaystyle{45}^{o}$ 
      $\displaystyle{\left(\frac{1}{{2}}\right)}{{\sin}^{2}{\left({22.5}^{o}\right)}}={0.0732}$
          $\displaystyle={0.1464}$
But the probability that one photon will pass at $\displaystyle{0}^{o}$ while the other will not pass at $\displaystyle{45}^{o}$ 
            $\displaystyle{\left(\frac{1}{{2}}\right)}{{\sin}^{2}{\left({45}^{o}\right)}}={0.25}$

It means $\displaystyle{0.25}>{0.0732}+{0.1464}$
A calcualtion that also apperas to agree well with experiment.
                 
         








## References:
[1][A. Einstein, B. Podolsky, N. Rosen: "Can quantum-mechanical description of physical reality be considered complete?" Physical Review 41, 777 (15 May 1935)]{https://cds.cern.ch/record/405662/files/PhysRev.47.777.pdf}
[2] {https://www.quantamagazine.org/how-bells-theorem-proved-spooky-action-at-a-distance-is-real-20210720/}
[3] {https://www.lesswrong.com/posts/AnHJX42C6r6deohTG/bell-s-theorem-no-epr-reality}

