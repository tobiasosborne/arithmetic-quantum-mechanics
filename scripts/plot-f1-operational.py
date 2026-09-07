#!/usr/bin/env python3
"""Render the Hecke subsystem-overlap figure; the exact checks are separate."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family":"serif", "mathtext.fontset":"cm", "font.size":11,
                     "pdf.fonttype":42, "axes.spines.top":False, "axes.spines.right":False})
fig,(diagram,ax)=plt.subplots(1,2,figsize=(10,3.6),gridspec_kw={"width_ratios":[1,1.2]})
diagram.set_axis_off()
box={"boxstyle":"round,pad=.55","fc":"#f2f5fa","ec":"#335c85","lw":1.2}
diagram.text(.23,.8,r"$\mathcal{A}_{12}\simeq\mathbb{C}^2$",ha="center",bbox=box)
diagram.text(.78,.8,r"$\mathcal{A}_{23}\simeq\mathbb{C}^2$",ha="center",bbox=box)
diagram.text(.5,.39,r"$\mathcal{A}_{123}\simeq\mathbb{C}\oplus\mathbb{C}\oplus M_2(\mathbb{C})$",
             ha="center",bbox=box)
for start in [(.25,.72),(.75,.72)]:
    diagram.annotate("",xy=(.5,.49),xytext=start,
                     arrowprops={"arrowstyle":"->","lw":1.5,"color":"#335c85"})
diagram.text(.5,.12,"The two embeddings retain the parameter\neven when the algebra types agree.",
             ha="center",va="center",fontsize=10)
diagram.set_title("Overlapping quantum subsystems",pad=12)
q=np.linspace(1,8,400)
ax.plot(q,q/(1+q)**2,color="#2255a4",lw=2)
for value,label in [(1,r"$1/4$"),(2,r"$2/9$"),(3,r"$3/16$"),(5,r"$5/36$")]:
    a=value/(1+value)**2
    ax.scatter([value],[a],s=38,color="#1b7f3b" if value==1 else "#2255a4",zorder=3)
    ax.annotate(label,(value,a),xytext=(7,7),textcoords="offset points",fontsize=11)
ax.set(xlim=(.8,8.2),ylim=(.08,.275),xlabel=r"Positive Hecke parameter $q$",
       ylabel=r"Intrinsic Born overlap $a(q)=q/(1+q)^2$")
ax.set_xticks([1,2,3,5,7])
ax.set_title(r"Finite fields: $q=p^m$; endpoint: $q=1$",pad=12)
ax.grid(axis="y",alpha=.2)
fig.tight_layout(w_pad=2.5)
target=Path(__file__).resolve().parents[1]/"labbook/figures/f1-operational-overlap.pdf"
target.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(target,bbox_inches="tight")
print(target)
