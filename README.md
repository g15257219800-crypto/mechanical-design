# Covering the unit disk with 100 equal disks

This repository records a **fully explicit algebraic covering** of the unit disk by 100 equal disks, together with a machine-checkable proof of covering. It does **not** claim that the construction is globally optimal: the exact value of \(r_D(100)\) is open.

## Theorems proved here

Let \(D=\{x\in\mathbb{R}^2:\lVert x\rVert_2\le 1\}\) and

\[
r_D(100)=\inf_{C\in(\mathbb{R}^2)^{100}}
\max_{x\in D}\min_{1\le i\le 100}\lVert x-c_i\rVert_2.
\]

1. **Polynomial and isolation.** \(P(t)=67t^2-1\) (coefficients \(-1,0,67\)) has exactly one real root in \(\bigl(\tfrac{3}{25},\tfrac18\bigr)\), namely \(\alpha=1/\sqrt{67}\).
2. **Construction.** Centers are the scaled hexagonal-lattice points
   \(c_{m,n}=\sqrt{3/67}\,p(m,n)\) for the 100 pairs \((m,n)\) in `data/centers_mn.txt`,
   i.e. all indices with \(m^2+mn+n^2\le 27\) plus the \(120^\circ\) orbit of \((4,2)\) on the shell of norm 28.
3. **Covering.** \(D\) is contained in the union of the 100 closed disks of radius \(\alpha\). The argument treats every point of \(D\), not a finite sample; the finite algebraic identities are checked in `src/verify_covering.py`.
4. **Bounds.** \(\tfrac1{10}<r_D(100)\le\alpha=1/\sqrt{67}\). Global equality \(r_D(100)=\alpha\) is **not** proved.

The full write-up is `PROOF.md`.

## Verify

```bash
python3 src/verify_covering.py
python3 src/plot_covering.py
```

Requires `sympy` and, for the figure, `matplotlib`.

## Status of the original problem

The problem asks for \(r_D(100)\) as the unique root of an integer polynomial, an explicit \(C_*\), a covering proof, and a proof that every competing configuration has covering radius at least that root, without assuming unproven symmetry. Parts 1–3 are completed for the **upper bound** \(\alpha\). Part 4 is completed only as the area bound \(1/10\). Proven optima in the literature stop at \(n=10\).
