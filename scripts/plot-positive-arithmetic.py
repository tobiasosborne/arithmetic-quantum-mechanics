#!/usr/bin/env python3
"""Illustrate the reviewed F2->F8 reference comparison; not a numerical proof."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root = Path(__file__).resolve().parents[1]
t = np.linspace(1, 2, 500)
old = 1 - 2 / t**2
state = (2 / 3) * (1 - 1 / t**2)
fig, ax = plt.subplots(figsize=(6.7, 3.4), layout="constrained")
ax.axhline(0, color="#777777", linewidth=0.8)
ax.fill_between(t, np.minimum(old, 0), 0, color="#bb4a3c", alpha=0.10)
ax.plot(t, state, color="#245c9c", linewidth=2.4,
        label=r"New state: $\frac{2}{3}(1-t^{-2})$")
ax.plot(t, old, color="#bb4a3c", linewidth=1.8, linestyle="--",
        label=r"Old formal trace: $1-2t^{-2}$")
ax.scatter([2], [0.5], color="#222222", s=24, zorder=5)
ax.annotate(r"Arithmetic point $t=p=2$", (2, 0.5), (1.6, 0.56),
            fontsize=9, ha="center",
            arrowprops={"arrowstyle": "->", "color": "#444444"})
ax.set(xlim=(0.98, 2.02), ylim=(-1.06, 0.66),
       xlabel=r"Counting parameter $t$ (actual characteristic $p=2$)",
       ylabel="Projection expectation")
ax.legend(loc="lower right", frameon=False, fontsize=10)
ax.spines[["top", "right"]].set_visible(False)
fig.savefig(root / "labbook/figures/positive-arithmetic-reference.pdf")
fig.savefig("/tmp/positive-arithmetic-reference.png", dpi=160)
