"""Top-down layout diagram for the EVA PLSS obstacle course.

Run: python3 course_layout.py
Output: ../demo/course-layout.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FIG_W, FIG_H = 12, 7.5
BG = "#f7f5fa"
ACCENT = "#6b5b95"   # muted purple
DARK = "#2e2a3b"
LIGHT_BOX = "#ffffff"
ARROW = "#8e7cc3"

stations = [
    ("STATION 1\nBolt torquing",
     "Drive 8 bolts with a power\n"
     "driver while wearing\n"
     "bulky work gloves.\n"
     "(PGT: 0.5-25.5 ft-lbs)"),
    ("STATION 2\nORU swap",
     "Carry a weighted 'ORU' box\nalong the handrail path.\n"
     "Remove old unit,\ninstall the new one."),
    ("STATION 3\nConnector mating",
     "Mate / demate 4 electrical\nconnectors — two of them\nblind (behind a panel)."),
    ("STATION 4\nCable routing",
     "Route a cable along the\nmarked path and secure\nit with 6 zip ties."),
]

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 12)
ax.set_ylim(0, 7.5)
ax.axis("off")

ax.text(6, 7.0, "EVA PLSS Obstacle Course — Layout",
        ha="center", va="center", fontsize=18, weight="bold", color=DARK)
ax.text(6, 6.55, "Constraints for every station: bulky gloves · limited mobility · tethered",
        ha="center", va="center", fontsize=11, style="italic", color=ACCENT)

# Start / finish markers
for x, label in ((0.7, "START"), (11.3, "FINISH")):
    ax.add_patch(FancyBboxPatch((x - 0.55, 2.35), 1.1, 0.9,
                                boxstyle="round,pad=0.08",
                                facecolor=ACCENT, edgecolor=ACCENT))
    ax.text(x, 2.8, label, ha="center", va="center",
            fontsize=11, weight="bold", color="white")

# Station boxes
box_w, box_h = 2.1, 3.4
centers_x = [2.9, 5.15, 7.4, 9.65]
y0 = 1.35
for cx, (title, body) in zip(centers_x, stations):
    ax.add_patch(FancyBboxPatch((cx - box_w / 2, y0), box_w, box_h,
                                boxstyle="round,pad=0.08",
                                facecolor=LIGHT_BOX, edgecolor=ACCENT,
                                linewidth=1.6))
    ax.text(cx, y0 + box_h - 0.35, title, ha="center", va="center",
            fontsize=11, weight="bold", color=DARK, linespacing=1.4)
    ax.plot([cx - box_w / 2 + 0.25, cx + box_w / 2 - 0.25],
            [y0 + box_h - 0.75, y0 + box_h - 0.75],
            color=ARROW, linewidth=1)
    ax.text(cx, y0 + box_h / 2 - 0.35, body, ha="center", va="center",
            fontsize=9.5, color=DARK, linespacing=1.5)

# Handrail path hint for station 2 (dashed line through the box bottom)
ax.plot([2.9 - box_w / 2 + 0.15, 2.9 + box_w / 2 - 0.15],
        [y0 + 0.28, y0 + 0.28], color=ARROW, linewidth=2,
        linestyle=(0, (4, 3)))
ax.text(2.9, y0 + 0.08, "handrail", ha="center", va="center",
        fontsize=8, style="italic", color=ACCENT)
ax.plot([5.15 - box_w / 2 + 0.15, 5.15 + box_w / 2 - 0.15],
        [y0 + 0.28, y0 + 0.28], color=ARROW, linewidth=2,
        linestyle=(0, (4, 3)))

# Flow arrows between stations
arrow_xs = [1.25, 4.02, 6.27, 8.52, 10.72]
for ax_ in arrow_xs:
    ax.add_patch(FancyArrowPatch((ax_, 2.8), (ax_ + 0.55, 2.8),
                                 arrowstyle="-|>", mutation_scale=16,
                                 color=ARROW, linewidth=1.6))

ax.text(6, 0.55, "Run it timed. Log station times — the 'what broke' section starts here.",
        ha="center", va="center", fontsize=10, style="italic", color=ACCENT)

plt.tight_layout()
plt.savefig("../demo/course-layout.svg", facecolor=BG,
            bbox_inches="tight")
print("saved ../demo/course-layout.svg")
