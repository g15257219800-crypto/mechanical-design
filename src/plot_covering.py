#!/usr/bin/env python3
"""Render the explicit 100-disk covering of the unit disk."""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "centers_mn.txt"
OUT = ROOT / "figures" / "covering_100.png"

SQRT3 = math.sqrt(3)
SCALE = math.sqrt(3 / 67)
ALPHA = 1 / math.sqrt(67)


def load_centers():
    pts = []
    with DATA.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            _, m, n = map(int, line.split())
            x = SCALE * (m + n / 2)
            y = SCALE * (n * SQRT3 / 2)
            pts.append((x, y))
    return pts


def main() -> None:
    pts = load_centers()
    assert len(pts) == 100
    OUT.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 8), dpi=160)
    ax.set_aspect("equal")
    ax.add_patch(
        Circle((0, 0), 1.0, fill=False, lw=2.0, color="black", zorder=3, label="unit disk")
    )
    for x, y in pts:
        ax.add_patch(
            Circle((x, y), ALPHA, fill=True, alpha=0.18, color="#d97706", lw=0.4, ec="#b45309")
        )
    xs, ys = zip(*pts)
    ax.scatter(xs, ys, s=8, c="#7c2d12", zorder=4, label="centers")
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ax.set_title(r"$100$ equal disks of radius $1/\sqrt{67}$ covering the unit disk")
    ax.legend(loc="upper right")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
