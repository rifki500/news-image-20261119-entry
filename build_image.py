#!/usr/bin/env python3
"""Draw entry.png: a newspaper front page summing up Thursday 19 Nov 2026.

Everything is drawn in code with PIL from the story data in this file:
no external photos, no network, no fonts beyond the DejaVu family that
ships with the operating system. Run:  python3 build_image.py
(writes entry.png next to this script)
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 233)
INK = (20, 20, 20)
RED = (172, 38, 28)
BLUE = (28, 74, 120)
TEAL = (14, 112, 104)
GREY = (92, 92, 92)
PALE = (233, 227, 212)
GOLD = (206, 164, 52)
ORANGE = (216, 110, 18)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def make_font(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, fnt, max_width):
    """Greedy word wrap; returns the lines that fit inside max_width."""
    out, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def draw_lines(draw, x, y, lines, fnt, fill=INK, leading=None):
    """Draw a list of lines; returns the y just below the block."""
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hrule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def star(draw, cx, cy, r, fill):
    """A small five-point star centred on (cx, cy)."""
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(pts, fill=fill)


# ---------------------------------------------------------------- visuals


def draw_scales(draw, x, y, w, h):
    """Scales of justice: a balance over a low plinth."""
    cx = x + w // 2
    base_y = y + h - 14
    # Plinth and post.
    draw.rectangle([x + 18, base_y, x + w - 18, base_y + 8], fill=INK)
    draw.rectangle([cx - 4, y + 34, cx + 4, base_y], fill=INK)
    # Crossbeam with a small finial.
    draw.rectangle([x + 8, y + 34, x + w - 8, y + 40], fill=INK)
    draw.ellipse([cx - 6, y + 24, cx + 6, y + 36], fill=RED)
    # Two pans hanging from the beam ends.
    for side in (-1, 1):
        px = cx + side * (w // 2 - 22)
        draw.line([(px, y + 40), (px - 20, y + 78)], fill=INK, width=2)
        draw.line([(px, y + 40), (px + 20, y + 78)], fill=INK, width=2)
        draw.line([(px, y + 40), (px, y + 78)], fill=INK, width=2)
        draw.chord([px - 22, y + 74, px + 22, y + 100], 0, 180, fill=BLUE)


def draw_three_flags(draw, x, y, w, h):
    """Three small flags side by side: China, Russia, United States."""
    fw = w // 3
    # China: red field, yellow dots for stars.
    draw.rectangle([x, y, x + fw - 5, y + h], fill=(222, 41, 16))
    for sx, sy in [(9, 9), (22, 7), (27, 15), (22, 24), (11, 21)]:
        draw.ellipse([x + sx - 3, y + sy - 3, x + sx + 3, y + sy + 3],
                     fill=(255, 222, 0))
    # Russia: white / blue / red horizontal bands.
    rx = x + fw
    draw.rectangle([rx, y, rx + fw - 5, y + h // 3], fill=(255, 255, 255),
                   outline=(170, 170, 170))
    draw.rectangle([rx, y + h // 3, rx + fw - 5, y + 2 * h // 3],
                   fill=(0, 57, 166))
    draw.rectangle([rx, y + 2 * h // 3, rx + fw - 5, y + h], fill=(213, 0, 50))
    # United States: stripes with a blue canton of dots.
    ux = x + 2 * fw
    for i in range(7):
        colour = (178, 34, 52) if i % 2 == 0 else (255, 255, 255)
        draw.rectangle([ux, y + i * h // 7, ux + fw - 5,
                        y + (i + 1) * h // 7], fill=colour)
    draw.rectangle([ux, y, ux + fw // 2, y + 4 * h // 7], fill=(60, 59, 110))
    for r in range(3):
        for c in range(3):
            dotx = ux + 6 + c * 9
            doty = y + 7 + r * 11
            draw.ellipse([dotx - 2, doty - 2, dotx + 2, doty + 2],
                         fill=(255, 255, 255))


def draw_globe_heat(draw, x, y, w, h):
    """A globe with a red arrow climbing past it: a warming world."""
    cx, cy = x + w // 2 - 14, y + h // 2 + 2
    r = 34
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=TEAL, width=3)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=TEAL,
                 width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=TEAL, width=2)
    draw.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 200, 340, fill=TEAL,
             width=2)
    # Rising arrow on the right.
    ax = x + w - 16
    draw.line([(ax, y + h - 12), (ax, y + 12)], fill=RED, width=4)
    draw.polygon([(ax - 9, y + 26), (ax + 9, y + 26), (ax, y + 6)], fill=RED)
    fnt = make_font(SANS_BOLD, 20)
    draw.text((x, y + h - 24), "1.5°C", font=fnt, fill=RED)


def draw_burning_house(draw, x, y, w, h):
    """A house with flames and smoke: arson in the unrest."""
    hx, hy = x + 14, y + 34
    hw, hh = w - 28, h - 44
    # Walls and roof.
    draw.rectangle([hx, hy + 22, hx + hw, hy + hh], fill=(226, 214, 190),
                   outline=INK, width=2)
    draw.polygon([(hx - 6, hy + 24), (hx + hw // 2, hy - 4),
                  (hx + hw + 6, hy + 24)], fill=INK)
    draw.rectangle([hx + hw // 2 - 9, hy + hh - 26, hx + hw // 2 + 9, hy + hh],
                   fill=INK)
    # Flames licking out of the roofline.
    for fx, fy, fs in [(hx + 16, hy + 8, 12), (hx + hw // 2, hy - 2, 15),
                       (hx + hw - 16, hy + 10, 11)]:
        draw.polygon([(fx - fs, fy + fs), (fx, fy - fs), (fx + fs, fy + fs),
                      (fx + fs // 2, fy + fs // 2),
                      (fx - fs // 2, fy + fs // 2)], fill=ORANGE)
        draw.polygon([(fx - fs // 2, fy + fs // 2), (fx, fy - fs // 2),
                      (fx + fs // 2, fy + fs // 2)], fill=(255, 214, 64))


def draw_rising_chart(draw, x, y, w, h):
    """Three rising bars and a climbing arrow: a record market debut."""
    # Axes.
    draw.line([(x + 6, y + h - 16), (x + w - 4, y + h - 16)], fill=INK, width=2)
    draw.line([(x + 6, y + 8), (x + 6, y + h - 16)], fill=INK, width=2)
    # Bars: low, middle, high.
    base = y + h - 16
    for i, bh in enumerate((26, 48, 70)):
        bx = x + 18 + i * 28
        draw.rectangle([bx, base - bh, bx + 20, base], fill=BLUE)
    # Arrow climbing over the bars.
    draw.line([(x + 12, base - 20), (x + w - 10, y + 14)], fill=RED, width=3)
    draw.polygon([(x + w - 26, y + 12), (x + w - 8, y + 10),
                  (x + w - 12, y + 28)], fill=RED)


def draw_eu_ring(draw, x, y, w, h):
    """A ring of twelve gold stars around a euro sign."""
    cx, cy = x + w // 2, y + h // 2 - 2
    r = 36
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=4)
    for i in range(12):
        ang = math.radians(i * 30 - 90)
        sx = cx + int((r - 2) * math.cos(ang))
        sy = cy + int((r - 2) * math.sin(ang))
        star(draw, sx, sy, 6, GOLD)
    fnt = make_font(SANS_BOLD, 30)
    label = "€"
    tw = draw.textlength(label, font=fnt)
    draw.text((cx - tw / 2, cy - 17), label, font=fnt, fill=BLUE)


def draw_tanker(draw, x, y, w, h):
    """A tanker on the waves with a blast above its deck."""
    # Sea.
    draw.rectangle([x, y + h - 20, x + w, y + h], fill=(122, 178, 204))
    for wy in (y + h - 14, y + h - 7):
        for wx in range(x, x + w, 16):
            draw.arc([wx, wy - 4, wx + 16, wy + 4], 180, 360, fill=BLUE)
    # Hull and funnel.
    hy = y + h - 44
    draw.polygon([(x + 4, hy), (x + w - 4, hy), (x + w - 18, hy + 24),
                  (x + 18, hy + 24)], fill=INK)
    draw.rectangle([x + w - 40, hy - 18, x + w - 24, hy], fill=RED)
    # Blast burst above the deck.
    bx, by = x + w // 2 - 8, y + 22
    burst = []
    for i in range(12):
        ang = math.radians(i * 30)
        rad = 16 if i % 2 == 0 else 8
        burst.append((bx + rad * math.cos(ang), by + rad * math.sin(ang)))
    draw.polygon(burst, fill=ORANGE)
    draw.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(255, 214, 64))


# ---------------------------------------------------------------- page


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # page margin

    # ---- Masthead.
    d.text((W // 2, 12), "THE WORLD TODAY", font=make_font(SERIF_BOLD, 60),
           fill=INK, anchor="ma")
    d.text((W // 2, 86), "THURSDAY, 19 NOVEMBER 2026",
           font=make_font(SANS_BOLD, 30), fill=RED, anchor="ma")
    d.text((W // 2, 122), "One day in the news  —  seven stories from around the world",
           font=make_font(SANS, 18), fill=GREY, anchor="ma")
    hrule(d, M, 150, W - M, 3)
    hrule(d, M, 156, W - M, 1)

    # ---- Lead story: the world court rules on the Rohingya.
    y = 168
    d.text((M, y), "THE HAGUE  ·  WORLD COURT", font=make_font(SANS_BOLD, 18),
           fill=RED)
    y += 27
    head = wrap_text(d, "World court: Myanmar committed genocide",
                     make_font(SERIF_BOLD, 38), W - M * 2 - 250)
    y = draw_lines(d, M, y, head, make_font(SERIF_BOLD, 38), leading=44)
    body = wrap_text(
        d,
        "The International Court of Justice rules Myanmar's military "
        "acted with genocidal intent against the Rohingya in 2017, "
        "and orders restitution for the survivors.",
        make_font(SANS, 20), W - M * 2 - 250)
    draw_lines(d, M, y + 6, body, make_font(SANS, 20), leading=26)
    draw_scales(d, W - M - 232, 196, 232, 132)
    d.text((W - M, 334), "The Peace Palace, The Hague",
           font=make_font(SANS_BOLD, 16), fill=GREY, anchor="ra")
    hrule(d, M, 396, W - M, 2)

    # ---- Grid of six stories: 2 columns x 3 rows.
    stories = [
        ("SHENZHEN  ·  SUMMIT", "Trump, Xi and Putin meet in first three-way summit",
         "The three leaders meet in Shenzhen and issue a joint "
         "'Declaration toward Peace' — but no deal on Ukraine or Iran.",
         draw_three_flags),
        ("ANTALYA  ·  CLIMATE", "COP31 draft drops fossil fuels",
         "A new draft deal removes every mention of moving away "
         "from coal, oil and gas, and admits the world will "
         "overshoot 1.5°C.",
         draw_globe_heat),
        ("DHAKA  ·  UNREST", "Bangladesh lockdown as violence spreads",
         "Hasina supporters try to shut the country down; "
         "Muhammad Yunus's ancestral home is torched and unrest "
         "hits 28 districts.",
         draw_burning_house),
        ("NEW YORK  ·  MARKETS", "Anthropic's record IPO soars on debut",
         "The AI firm behind Claude lists on Nasdaq at $83, opens "
         "at $111.50 and raises $81bn — the largest IPO ever.",
         draw_rising_chart),
        ("BRUSSELS  ·  EUROPE", "EU proposes €45bn loan for Ukraine",
         "The European Commission proposes a new loan to cover "
         "two-thirds of Kyiv's 2027 funding gap: €25bn military, "
         "€20bn civilian.",
         draw_eu_ring),
        ("THE GULF  ·  ENERGY", "Hormuz tanker attacks mount",
         "More ships are hit in the Strait of Hormuz as US–Iran "
         "strikes escalate; an ADNOC vessel is attacked, 11 crew "
         "hurt, one missing.",
         draw_tanker),
    ]
    col_w = (W - M * 2 - 24) // 2
    row_h = 172
    for i, (kicker, headline, summary, visual) in enumerate(stories):
        col, row = i % 2, i // 2
        x0 = M + col * (col_w + 24)
        y0 = 410 + row * row_h
        if col == 1:
            d.line([(x0 - 12, y0 + 4), (x0 - 12, y0 + row_h - 18)],
                   fill=GREY, width=1)
        vw, vh = 112, 100
        visual(d, x0, y0 + 6, vw, vh)
        tx = x0 + vw + 12
        tw = col_w - vw - 12
        d.text((tx, y0), kicker, font=make_font(SANS_BOLD, 15), fill=RED)
        hl = wrap_text(d, headline, make_font(SERIF_BOLD, 25), tw)
        yy = draw_lines(d, tx, y0 + 22, hl, make_font(SERIF_BOLD, 25),
                        leading=29)
        sl = wrap_text(d, summary, make_font(SANS, 17), tw)
        draw_lines(d, tx, yy + 4, sl, make_font(SANS, 17), leading=22)
        if row < 2:
            hrule(d, x0, y0 + row_h - 10, x0 + col_w, 1, (198, 192, 176))

    # ---- Footer.
    hrule(d, M, 940, W - M, 2)
    d.text((M, 952),
           "Sources: ICJ · Reuters · AP · UN News · WSJ · NPR · Al Jazeera",
           font=make_font(SANS, 14), fill=GREY)
    d.text((M, 972),
           "All events of Thursday, 19 November 2026.",
           font=make_font(SANS_BOLD, 14), fill=GREY)
    d.text((W - M, 952), "THE WORLD TODAY", font=make_font(SANS_BOLD, 14),
           fill=GREY, anchor="ra")

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, "PNG")
    print("wrote", out, img.size, out.stat().st_size, "bytes")


if __name__ == "__main__":
    build()
