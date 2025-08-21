# Free Will Theorem Project

This repository gathers a collection of Python scripts dedicated to the study of the **Free Will Theorem** of Conway & Kochen.  
The project focuses on **Peres’ 33 directions**, their orthogonality relations, and the **Kochen–Specker–Conway–Abramsky (KSCA) lemma**, with both computational and graphical explorations.

---

## Contents

1. [Peres’ 33 Directions](#peres-33-directions--peres33directionspy)  
2. [Orthogonality Function](#orthogonality-function--orthogonalitepy)  
3. [Questions on Orthogonality](#questions-on-orthogonality--questionspy)  
4. [Graph Visualization](#graph-visualization--graph2dpy)  
5. [Brute-Force Proof of KSCA Lemma](#brute-force-proof-of-ksca-lemma--forcebrutepy)  
6. [Coordinate Converter](#coordinate-converter--convertisseurpy)  
7. [Abramsky Approach](#abramsky-approach--abramskypy)  
8. [Orbits and Symmetries](#orbits-and-symmetries--orbitespy)

---

## Theoretical Background

The **Free Will Theorem** relies on three axioms:

* **SPIN** – Certain triples of squared spin-1 operators always sum to 2.
* **TWIN** – Pairs of entangled particles (twins) give correlated results, even at a distance.
* **MIN** – Measurement choices are free and independent from prior information.

From these, Conway and Kochen prove that if experimenters have free will in choosing measurements, then elementary particles must also possess a kind of "free will".

This project implements computational tools to visualize and verify the structures underlying these ideas.

---

## Peres’ 33 Directions — [Peres33Directions.py](Peres33Directions.py)

This module generates the **33 Peres directions**, a canonical set of vectors in 3D space used to formulate the Kochen–Specker argument.  
It includes filtering utilities to restrict to specific cube faces.

![1](https://github.com/Toppics/Directions-de-Peres/assets/110732997/8f579ba4-638a-4ebc-9111-4a110a95d5b7)  
![2](https://github.com/Toppics/Directions-de-Peres/assets/110732997/0553746e-8000-4bfb-a03d-b93ee3a18eaf)

---

## Orthogonality Function — [orthogonalite.py](orthogonalite.py)

This script defines a utility function to check whether a set of vectors is **mutually orthogonal** (generalized dot product equal to zero).  
It works for **pairs, triplets, or larger collections of vectors**.

---

## Questions on Orthogonality — [questions.py](questions.py)

Builds upon the orthogonality function to:  

* Identify the **16 orthogonal triplets** among Peres’ directions  
* Extract all **72 orthogonal pairs**  
* Filter out pairs already contained in triplets  
* Generate the **24 additional triplets** needed to complete the structure  

![Q8 1](https://github.com/Toppics/Directions-de-Peres/assets/110732997/fd265721-a41c-4c08-aa8e-8e4e2d55d1ff)

---

## Graph Visualization — [Graph2D.py](Graph2D.py)

Constructs the **orthogonality graph**:  

* Vertices represent Peres’ directions  
* Edges connect orthogonal vectors  
* Useful to study planarity, connectivity, and graph-theoretical aspects of the problem  

![Graphe](https://github.com/Toppics/Directions-de-Peres/assets/110732997/4187a8d6-f923-43a7-ab22-47fa505911a3)

---

## Brute-Force Proof of KSCA Lemma — [ForceBrute.py](ForceBrute.py)

Implements an **exhaustive search** of all possible functions  
\[
\gamma: P \to \{0,1\}
\]  
to verify the conditions of the KSCA lemma and confirm the **impossibility of a “101-function”**.

---

## Coordinate Converter — [convertisseur.py](convertisseur.py)

Converts lists of floating-point coordinates from Python into **exact symbolic expressions** (square roots, fractions) compatible with **SageMath**.  
This enables rigorous symbolic computations and proofs.

---

## Abramsky Approach — [abramsky.py](abramsky.py)

Reformulates the KSCA lemma using **Abramsky’s database-theoretic perspective**, connecting the combinatorial constraints of Peres’ directions with contextuality in quantum mechanics.

---

## Orbits and Symmetries — [orbites.py](orbites.py)

Explores the **orbits of Peres’ directions, triplets, and pairs** under the action of the **cube’s rotation group** (24 symmetries).  
This reveals the equivalence classes of directions and structures under symmetry.

---

## Requirements

All scripts are written in **Python 3** and rely mainly on:

```bash
pip install numpy matplotlib networkx
```

Optional: **SageMath** (for symbolic coordinate checks).

---

## References

* Conway J., Kochen S. (2006), *The Free Will Theorem*, Foundations of Physics.
* Peres A. (1991), *Two simple proofs of the Kochen-Specker theorem*, J. Phys. A.
* Abramsky S., Brandenburger A. (2011), *The sheaf-theoretic structure of non-locality and contextuality*.
* Course Material: *MT33 – Free Will Theorem*.
