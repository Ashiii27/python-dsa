#!/usr/bin/env python3
"""Compose the social preview card (og.png) for Python DSA Masterclass.

Design mirrors the site identity: warm cream paper with grain, ink text,
Fraunces display serif (italic accent), JetBrains Mono details, terracotta
badge matching the logo.

Fonts (SIL OFL, from the google/fonts repository) are read from --fonts-dir:

    Fraunces[SOFT,WONK,opsz,wght].ttf
    Fraunces-Italic[SOFT,WONK,opsz,wght].ttf
    JetBrainsMono[wght].ttf

Usage:
    python3 scripts/make_og.py --fonts-dir /tmp/ogfonts --out static/img/og.png
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
SCALE = 2  # supersample factor

PAPER = (250, 245, 236)
INK = (36, 29, 21)
INK_SOFT = (107, 95, 80)
CLAY = (180, 85, 46)
CLAY_DEEP = (156, 69, 35)
AMBER = (217, 144, 61)
PINE = (46, 107, 76)
WHITE = (255, 253, 248)


def set_axes(font: ImageFont.FreeTypeFont, **want: float) -> None:
    try:
        axes = font.get_variation_axes()
    except Exception:
        return
    values = []
    for axis in axes:
        name = axis["name"].decode() if isinstance(axis["name"], bytes) else str(axis["name"])
        values.append(float(want.get(name, axis["default"])))
    try:
        font.set_variation_by_axes(values)
    except Exception:
        pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    fonts = Path(args.fonts_dir)

    fraunces = str(next(fonts.glob("Fraunces[*.ttf")))
    fraunces_it = str(next(fonts.glob("Fraunces-Italic[*.ttf")))
    mono = str(next(fonts.glob("JetBrainsMono[*.ttf")))

    img = Image.new("RGB", (W * SCALE, H * SCALE), PAPER)
    d = ImageDraw.Draw(img, "RGBA")

    # ---- warm glow, top-right ----
    glow = Image.new("RGB", (W * SCALE, H * SCALE), PAPER)
    gd = ImageDraw.Draw(glow)
    gd.ellipse(
        (1350 * SCALE, -420 * SCALE, 2350 * SCALE, 560 * SCALE),
        fill=(244, 222, 190),
    )
    glow = glow.resize((W * SCALE, H * SCALE))
    img = Image.blend(img, glow, 0.55)
    d = ImageDraw.Draw(img, "RGBA")

    # ---- decorative algorithm curves (low-contrast sine strokes) ----
    for (amp, y_off, width, color, alpha, lam) in [
        (46, 470, 6, PINE, 42, 300),
        (30, 520, 5, AMBER, 60, 240),
    ]:
        pts = [
            (x, y_off + amp * math.sin(x / lam * math.pi * 2 + 0.8))
            for x in range(120 * SCALE, (W - 130) * SCALE, 8)
        ]
        d.line(pts, fill=(*color, alpha), width=width * SCALE, joint="curve")

    # ---- badge with gradient (matches the logo) ----
    bx, by, bs = 880, 150, 230
    grad = Image.new("RGB", (bs * SCALE, bs * SCALE))
    for y in range(bs * SCALE):
        t = y / (bs * SCALE)
        c = tuple(int(CLAY[i] + (AMBER[i] - CLAY[i]) * t) for i in range(3))
        grad.paste(Image.new("RGB", (bs * SCALE, 1), c), (0, y))
    mask = Image.new("L", (bs * SCALE, bs * SCALE), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, bs * SCALE, bs * SCALE), radius=56 * SCALE, fill=255
    )
    img.paste(grad, (bx * SCALE, by * SCALE), mask)
    d = ImageDraw.Draw(img, "RGBA")

    mono_big = ImageFont.truetype(mono, 86 * SCALE)
    set_axes(mono_big, wght=700)
    d.text(
        ((bx + bs / 2) * SCALE, (by + bs / 2) * SCALE),
        "</>",
        font=mono_big,
        fill=WHITE,
        anchor="mm",
    )
    # soft scribble under the glyph, like the logo
    d.arc(
        ((bx + 34) * SCALE, (by + 130) * SCALE, (bx + bs - 34) * SCALE, (by + 215) * SCALE),
        start=15,
        end=165,
        fill=(255, 253, 248, 190),
        width=5 * SCALE,
    )

    # ---- eyebrow ----
    mono_sm = ImageFont.truetype(mono, 21 * SCALE)
    set_axes(mono_sm, wght=600)
    d.text(
        (110 * SCALE,
        118 * SCALE),
        "OPEN SOURCE  ·  TWO TRACKS  ·  LEARN BY RUNNING CODE",
        font=mono_sm,
        fill=CLAY_DEEP,
    )
    d.line(
        (110 * SCALE, 150 * SCALE, 260 * SCALE, 150 * SCALE),
        fill=(*CLAY, 220),
        width=4 * SCALE,
    )

    # ---- title ----
    f_title = ImageFont.truetype(fraunces, 96 * SCALE)
    set_axes(f_title, wght=640, opsz=100)
    f_ital = ImageFont.truetype(fraunces_it, 96 * SCALE)
    set_axes(f_ital, wght=640, opsz=100)

    d.text((110 * SCALE, 236 * SCALE), "Python DSA", font=f_title, fill=INK, anchor="ls")
    width_first = d.textlength("Python DSA ", font=f_title)
    d.text((110 * SCALE, 350 * SCALE), "Masterclass", font=f_ital, fill=CLAY_DEEP, anchor="ls")

    # hand-drawn squiggle under "Masterclass"
    sq_w = d.textlength("Masterclass", font=f_ital)
    y0 = 378
    pts = [
        (110 * SCALE + x, (y0 + 7 * math.sin(x / (sq_w / 3.2) * math.pi * 2)) * SCALE)
        for x in range(0, int(sq_w), 10)
    ]
    d.line(pts, fill=(*AMBER, 235), width=6 * SCALE, joint="curve")

    # ---- subtitle ----
    f_sub = ImageFont.truetype(mono, 27 * SCALE)
    set_axes(f_sub, wght=500)
    d.text(
        (110 * SCALE,
        452 * SCALE),
        "From your first Python program to top-tier interview readiness.",
        font=f_sub,
        fill=INK_SOFT,
        anchor="ls",
    )

    # ---- stats footer ----
    f_stat = ImageFont.truetype(mono, 22 * SCALE)
    set_axes(f_stat, wght=700)
    f_stat_lab = ImageFont.truetype(mono, 22 * SCALE)
    set_axes(f_stat_lab, wght=500)
    x = 110
    stats = [
        ("12", "Python modules"),
        ("24", "DSA topics"),
        ("35", "worked problems"),
        ("280+", "practice problems"),
    ]
    for i, (num, label) in enumerate(stats):
        d.text((x * SCALE, 536 * SCALE), num, font=f_stat, fill=CLAY_DEEP, anchor="ls")
        nx = x + d.textlength(num, font=f_stat) / SCALE + 10
        d.text((nx * SCALE, 536 * SCALE), label, font=f_stat_lab, fill=INK_SOFT, anchor="ls")
        x = nx + d.textlength(label, font=f_stat_lab) / SCALE + 34
        if i < len(stats) - 1:
            d.ellipse(
                ((x - 20) * SCALE, 534 * SCALE, (x - 12) * SCALE, 542 * SCALE),
                fill=(*AMBER, 220),
            )

    # ---- paper grain ----
    noise = Image.effect_noise((W, H), 22).convert("L").resize((W * SCALE, H * SCALE))
    grain = Image.merge("RGB", (noise, noise, noise))
    img = Image.blend(img, grain, 0.055)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(out, "PNG", optimize=True)
    print(f"make_og: wrote {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
