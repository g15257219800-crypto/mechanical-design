#!/usr/bin/env python3
"""Exact certificate for the 100-disk covering of the unit disk.

Proves, using only integer and Q(sqrt(3)) arithmetic (via sympy):

  * the index set S has 100 points, uniquely specified;
  * the covering radius of the infinite hexagonal lattice of spacing 1 is 1/sqrt(3);
  * Voronoi cells of lattice points with m^2+mn+n^2 >= 31 miss the disk of
    radius sqrt(67/3);
  * each of the 9 unselected shell-28 Voronoi cells meets that disk only at a
    single vertex V with |V|^2 = 67/3, and V is within 1/sqrt(3) of two points
    of S;
  * those cells lie in the supporting half-space x·V >= |V|^2, hence the disk
    meets them only at V.

Together these facts prove that the scaled configuration C* covers the unit
disk with radius alpha = 1/sqrt(67).  See PROOF.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "centers_mn.txt"

SQRT3 = sp.sqrt(3)
HALF = sp.Rational(1, 2)
NEIGHBORS_CYCLIC = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
ROT120 = lambda m, n: (-m - n, m)  # 120 degree lattice rotation
SEED_28 = (4, 2)
ORBIT_28 = (SEED_28, ROT120(*SEED_28), ROT120(*ROT120(*SEED_28)))


def qnorm(m: int, n: int) -> int:
    return m * m + m * n + n * n


def pos(m: int, n: int):
    return (m + n * HALF, n * SQRT3 / 2)


def load_indices():
    pairs = []
    with DATA.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            q, m, n = map(int, line.split())
            assert q == qnorm(m, n), (q, m, n)
            pairs.append((m, n))
    return pairs


def lattice_disk(max_q: int):
    pts = []
    bound = int(max_q**0.5) + 2
    for m in range(-bound, bound + 1):
        for n in range(-bound, bound + 1):
            if qnorm(m, n) <= max_q:
                pts.append((m, n))
    return pts


def voronoi_vertices(u):
    pu = pos(*u)
    verts = []
    for i, d1 in enumerate(NEIGHBORS_CYCLIC):
        d2 = NEIGHBORS_CYCLIC[(i + 1) % 6]
        v1 = (u[0] + d1[0], u[1] + d1[1])
        v2 = (u[0] + d2[0], u[1] + d2[1])
        p1, p2 = pos(*v1), pos(*v2)
        cc = ((pu[0] + p1[0] + p2[0]) / 3, (pu[1] + p1[1] + p2[1]) / 3)
        verts.append((sp.simplify(cc[0]), sp.simplify(cc[1]), v1, v2))
    return verts


def check_unique_root():
    t = sp.symbols("t")
    P = 67 * t**2 - 1
    a, b = sp.Rational(3, 25), sp.Rational(1, 8)
    assert P.subs(t, a) < 0
    assert P.subs(t, b) > 0
    # strictly increasing on [0, inf)
    assert sp.diff(P, t) == 134 * t
    roots = sp.roots(P)
    real_in_interval = [
        r for r in roots if r.is_real and r > a and r < b
    ]
    assert len(real_in_interval) == 1
    assert sp.simplify(real_in_interval[0] ** 2 - sp.Rational(1, 67)) == 0
    return P, a, b, real_in_interval[0]


def check_kershner_style_gap():
    """sqrt(31) - 1/sqrt(3) > sqrt(67/3), so N>=31 cells miss the disk."""
    lhs = 3 * sp.sqrt(31) - sp.sqrt(3)
    rhs = sp.sqrt(201)
    # both sides positive; compare squares
    left_sq = sp.simplify(lhs**2)  # 282 - 6*sqrt(93)
    right_sq = sp.simplify(rhs**2)  # 201
    # 282 - 6 sqrt(93) > 201  <=>  81 > 6 sqrt(93)  <=>  27/2 > sqrt(93)
    # <=>  729/4 > 93  <=>  729 > 372
    assert sp.Integer(729) > sp.Integer(372)
    assert left_sq - right_sq == 81 - 6 * sp.sqrt(93)
    assert sp.simplify((sp.Rational(27, 2)) ** 2 - 93) == sp.Rational(729, 4) - 93
    assert sp.Rational(729, 4) - 93 == sp.Rational(357, 4)
    assert sp.Rational(357, 4) > 0
    return True


def main() -> int:
    errors = []

    pairs = load_indices()
    if len(pairs) != 100:
        errors.append(f"expected 100 centers, got {len(pairs)}")
    if len(set(pairs)) != len(pairs):
        errors.append("duplicate lattice indices")

    inner = lattice_disk(27)
    if len(inner) != 97:
        errors.append(f"q<=27 should have 97 points, got {len(inner)}")

    orbit = tuple(sorted(ORBIT_28))
    if orbit != tuple(sorted((( -6, 4), (2, -6), (4, 2)))):
        errors.append(f"120-degree orbit of (4,2) is {orbit}")

    expected = set(inner) | set(ORBIT_28)
    if set(pairs) != expected:
        errors.append("index file does not match q<=27 plus orbit of (4,2)")

    # Unique specification: no other q=28 point lies in S.
    extra = [p for p in pairs if qnorm(*p) == 28]
    if set(extra) != set(ORBIT_28):
        errors.append(f"q=28 points in S are {extra}")

    P, a, b, alpha = check_unique_root()
    print(f"P(t) = {P}")
    print("coefficients [t^0, t^1, t^2] = [-1, 0, 67]")
    print(f"unique positive root in ({a}, {b}): alpha = {alpha} = 1/sqrt(67)")

    check_kershner_style_gap()
    print("N>=31 Voronoi cells miss the unscaled disk (exact square comparison).")

    S = set(pairs)
    unselected_28 = []
    bound = 8
    for m in range(-bound, bound + 1):
        for n in range(-bound, bound + 1):
            if qnorm(m, n) == 28 and (m, n) not in S:
                unselected_28.append((m, n))
    if len(unselected_28) != 9:
        errors.append(f"expected 9 unselected q=28 points, got {len(unselected_28)}")

    R2 = sp.Rational(67, 3)
    rho2 = sp.Rational(1, 3)  # (1/sqrt(3))^2

    for u in sorted(unselected_28):
        verts = voronoi_vertices(u)
        on_circle = []
        inside = []
        for x, y, v1, v2 in verts:
            r2 = sp.simplify(x**2 + y**2)
            if r2 == R2:
                on_circle.append((x, y, v1, v2))
            elif r2 < R2:
                inside.append((x, y, r2, v1, v2))
        if inside:
            errors.append(f"{u}: Voronoi vertex strictly inside the disk: {inside}")
        if len(on_circle) != 1:
            errors.append(f"{u}: expected one vertex on the circle, got {on_circle}")
            continue
        Vx, Vy, v1, v2 = on_circle[0]
        if v1 not in S or v2 not in S:
            errors.append(f"{u}: boundary vertex neighbors {v1}, {v2} not both in S")
        # distance from V to each of v1, v2, u equals 1/sqrt(3)
        for w in (u, v1, v2):
            px, py = pos(*w)
            d2 = sp.simplify((Vx - px) ** 2 + (Vy - py) ** 2)
            if d2 != rho2:
                errors.append(f"{u}: dist^2 from V to {w} is {d2}, not 1/3")
        # supporting half-space: every vertex W satisfies W·V >= |V|^2
        for x, y, _, _ in verts:
            gap = sp.simplify(x * Vx + y * Vy - R2)
            if gap < 0:
                errors.append(f"{u}: supporting half-space fails, gap={gap}")

    print(f"checked {len(unselected_28)} unselected shell-28 cells exactly.")

    # Lattice covering radius identity: equilateral triangle of side 1.
    A, B, C = pos(0, 0), pos(1, 0), pos(0, 1)
    ccx = (A[0] + B[0] + C[0]) / 3
    ccy = (A[1] + B[1] + C[1]) / 3
    cr2 = sp.simplify((ccx - A[0]) ** 2 + (ccy - A[1]) ** 2)
    if cr2 != rho2:
        errors.append(f"unit-triangle circumradius^2 is {cr2}, not 1/3")
    print("hexagonal lattice covering radius is exactly 1/sqrt(3).")

    if errors:
        print("FAILED:")
        for e in errors:
            print("  -", e)
        return 1

    print("All exact checks passed.")
    print("Therefore the configuration C* covers the unit disk with radius 1/sqrt(67).")
    print("Hence r_D(100) <= 1/sqrt(67).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
