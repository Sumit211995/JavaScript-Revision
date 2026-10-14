#!/usr/bin/env python3
"""Create branded images for the Tata Motors report (educational graphics)."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "images"
OUT.mkdir(parents=True, exist_ok=True)
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def tata_logo():
    w, h = 520, 180
    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([10, 20, 510, 160], radius=18, outline="#003366", width=4, fill="#f7fafc")
    d.rounded_rectangle([30, 45, 200, 135], radius=8, fill="#003366")
    fb = ImageFont.truetype(FONT_B, 46)
    d.text((52, 58), "TATA", fill="white", font=fb)
    fm = ImageFont.truetype(FONT_B, 34)
    d.text((220, 62), "MOTORS", fill="#003366", font=fm)
    fs = ImageFont.truetype(FONT, 16)
    d.text((222, 108), "India's Automotive Leader", fill="#555555", font=fs)
    img.save(OUT / "tata_logo_brand.png")


def detailed_history():
    fig, ax = plt.subplots(figsize=(10, 11), dpi=150)
    events = [
        (1945, "TELCO incorporated; locomotive & engineering"),
        (1954, "Commercial vehicles with Daimler-Benz"),
        (1986, "Iconic Tata 407 LCV"),
        (1991, "Tata Sierra - entry into passenger vehicles"),
        (1998, "Tata Indica - first fully indigenous Indian car"),
        (2004, "Daewoo Commercial Vehicles acquisition (Korea)"),
        (2005, "Tata Ace - India's first mini truck"),
        (2008, "Jaguar Land Rover acquired from Ford"),
        (2016, "Tiago & IMPACT design philosophy"),
        (2019, "Nexon EV with ZIPTRON technology"),
        (2020, "BS VI transition; Safari relaunch"),
        (2023, "Ford Sanand plant acquisition; capacity expansion"),
        (2024, "acti.ev platform; 6M+ cumulative PV sales milestone"),
        (2025, "Curvv, Nexon iCNG; CV-PV demerger; Tamil Nadu plant"),
    ]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(events) + 1)
    ax.axvline(2.2, color="#c8102e", lw=3)
    for i, (year, text) in enumerate(reversed(events)):
        y = i + 1
        ax.scatter([2.2], [y], s=120, c="#003366", zorder=3)
        ax.text(2.45, y, str(year), fontsize=10, fontweight="bold", va="center")
        ax.text(3.2, y, text, fontsize=8.5, va="center")
    ax.axis("off")
    ax.set_title("Detailed History & Development of Tata Motors", fontsize=14, fontweight="bold", pad=12)
    plt.tight_layout()
    plt.savefig(OUT / "history_detailed.png", bbox_inches="tight")
    plt.close()


def product_showcase():
    fig, axes = plt.subplots(2, 3, figsize=(11, 6.5), dpi=150)
    products = [
        ("Nexon / Nexon EV", "Compact SUV\nZIPTRON EV", "#0066aa"),
        ("Harrier / Safari", "Premium SUV\nLand Rover derived", "#003366"),
        ("Tiago / Altroz", "Hatchback\nCity mobility", "#5c6bc0"),
        ("Tata Ace / Intra", "SCV & LCV\nLast-mile logistics", "#2e7d32"),
        ("Prima / Signa", "Heavy trucks\nLong haul", "#455a64"),
        ("Starbus / e-Bus", "Passenger transport\nSmart city EV", "#00897b"),
    ]
    for ax, (name, desc, col) in zip(axes.flat, products):
        ax.set_facecolor("#f5f8fb")
        ax.add_patch(mpatches.FancyBboxPatch((0.08, 0.12), 0.84, 0.76, boxstyle="round,pad=0.03", fc="white", ec=col, lw=2.5))
        ax.add_patch(mpatches.Rectangle((0.08, 0.62), 0.84, 0.26, fc=col, alpha=0.9))
        ax.text(0.5, 0.75, name, ha="center", va="center", color="white", fontsize=10, fontweight="bold")
        ax.text(0.5, 0.38, desc, ha="center", va="center", fontsize=9, color="#333")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
    fig.suptitle("Key Products Manufactured by Tata Motors (Representative Portfolio)", fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT / "products_showcase.png", bbox_inches="tight")
    plt.close()


def internship_infographic():
    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    ax.axis("off")
    ax.set_title("Why Internship at Tata Motors? (ECE / Diploma Students)", fontweight="bold", fontsize=13)
    boxes = [
        (0.05, 0.55, "Real plant exposure\nPune, Sanand, Jamshedpur"),
        (0.36, 0.55, "Electrical & electronics\nHarness, ECU, BMS, testing"),
        (0.67, 0.55, "Lean / quality culture\nSafety-first manufacturing"),
        (0.05, 0.12, "Student programmes\nCampus & institute tie-ups"),
        (0.36, 0.12, "Mentorship\nCross-functional teams"),
        (0.67, 0.12, "Career pathway\nGET & technical roles"),
    ]
    for x, y, t in boxes:
        ax.add_patch(mpatches.FancyBboxPatch((x, y), 0.28, 0.32, boxstyle="round", fc="#e3f2fd", ec="#1565c0"))
        ax.text(x + 0.14, y + 0.16, t, ha="center", va="center", fontsize=8.5)
    plt.tight_layout()
    plt.savefig(OUT / "internship_value.png", bbox_inches="tight")
    plt.close()


def cover_premium():
    w, h = 1400, 520
    img = Image.new("RGB", (w, h), "#0a2744")
    d = ImageDraw.Draw(img)
    d.polygon([(0, h), (w, h), (w, h - 120), (0, h - 40)], fill="#c8102e")
    d.rectangle([0, 0, w, 12], fill="#c8102e")
    fb = ImageFont.truetype(FONT_B, 72)
    fs = ImageFont.truetype(FONT, 28)
    d.text((70, 90), "TATA MOTORS LIMITED", fill="white", font=fb)
    d.text((70, 185), "Company Research Report | Diploma Internship", fill="#d0e4ff", font=fs)
    d.text((70, 240), "Automotive Products | History | R&D | Manufacturing", fill="#b0c4de", font=fs)
    d.rounded_rectangle([980, 60, 1330, 200], radius=16, fill="white")
    d.text((1010, 95), "TATA", fill="#003366", font=ImageFont.truetype(FONT_B, 54))
    d.text((1010, 150), "MOTORS", fill="#003366", font=ImageFont.truetype(FONT_B, 32))
    img.save(OUT / "cover_premium.png")


if __name__ == "__main__":
    tata_logo()
    detailed_history()
    product_showcase()
    internship_infographic()
    cover_premium()
    print("brand assets ok")
