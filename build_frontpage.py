#!/usr/bin/env python3
"""Build the 23 November 2026 world-news front page (1024x1024).

All text is rendered with real fonts (PIL), so no headline is ever garbled:
the AI-generated illustration is used only as the hero photograph panel.
Output: entry.png next to this script (JPEG bytes inside a .png name are NOT
used here; we save a real PNG, and fall back to JPEG only if > 1 MiB).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1024, 1024
MARGIN = 28
INNER = W - 2 * MARGIN  # 968
PAPER = (253, 252, 247)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (20, 48, 92)
GREY = (90, 90, 90)
LIGHT = (238, 236, 228)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning list of lines that fit `width` px."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer border
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=4)

    y = 20
    # --- masthead ---
    f_mast = font(SERIF_B, 62)
    mast = "THE WORLD TODAY"
    d.text(((W - d.textlength(mast, font=f_mast)) / 2, y), mast,
           font=f_mast, fill=INK)
    y += 76
    d.rectangle([MARGIN, y, W - MARGIN, y + 4], fill=RED)
    y += 12

    # --- date strip (black bar, white text) ---
    f_date = font(SANS_B, 23)
    date_txt = "MONDAY, 23 NOVEMBER 2026  •  THE DAY IN WORLD NEWS"
    d.rectangle([MARGIN, y, W - MARGIN, y + 40], fill=INK)
    d.text(((W - d.textlength(date_txt, font=f_date)) / 2, y + 7),
           date_txt, font=f_date, fill=(255, 255, 255))
    y += 52

    # --- hero photo (AI illustration, cropped to fill) ---
    hero = Image.open("hero.png").convert("RGB")
    hero = ImageOps.fit(hero, (INNER, 268), method=Image.LANCZOS)
    img.paste(hero, (MARGIN, y))
    d.rectangle([MARGIN, y, W - MARGIN, y + 268], outline=INK, width=2)
    y += 268 + 6
    f_cap = font(SANS_I, 14)
    cap = ("Ukrainian sea drones struck the Russian corvette Merkury "
           "off Benghazi, Libya.  Illustration.")
    d.text((MARGIN, y), cap, font=f_cap, fill=GREY)
    y += 24

    # --- lead headline + subhead ---
    f_head = font(SANS_B, 37)
    head = "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA"
    # shrink until it fits one line
    while d.textlength(head, font=f_head) > INNER and f_head.size > 28:
        f_head = font(SANS_B, f_head.size - 1)
    d.text((MARGIN, y), head, font=f_head, fill=INK)
    y += 48
    f_sub = font(SANS, 19)
    sub = ("President Zelenskyy confirms the sea-drone strike on the corvette "
           "Merkury and a hit on a Russian cargo ship — the war reaches "
           "Africa's shores.")
    y = draw_lines(d, wrap(d, sub, f_sub, INNER), MARGIN, y, f_sub, INK, 25)
    y += 8
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=2)
    y += 12

    # --- 2x2 story grid ---
    stories = [
        ("UKRAINE", RED, "Russian strikes kill at least 15 near Kyiv",
         "A drone strike wrecked a block of flats in Dymer; rescuers pulled "
         "a boy, 7, and a woman, 79, alive from the rubble."),
        ("CLIMATE", (0, 110, 70), "COP31 ends with no climate deal",
         "UN talks in Turkey closed without agreement on fossil fuels or "
         "finance — the longest climate summit in history."),
        ("EUROPE", NAVY, "NATO meets as Russian missiles enter Poland",
         "Poland called emergency talks after three objects crossed its "
         "airspace. NATO vows to defend \u2018every inch\u2019 of its territory."),
        ("MIDDLE EAST", (122, 60, 140), "Trump rejects Iran's deal as Bahrain is hit",
         "Trump said Iran wants a deal but not one \u2018acceptable\u2019 to him, "
         "as an Iranian attack struck a civilian site in Bahrain."),
    ]
    col_w = (INNER - 24) // 2
    row_h = 132
    f_kick = font(SANS_B, 14)
    f_sh = font(SANS_B, 21)
    f_sb = font(SANS, 16)
    for i, (kick, color, sh, sb) in enumerate(stories):
        cx = MARGIN + (i % 2) * (col_w + 24)
        cy = y + (i // 2) * (row_h + 10)
        d.text((cx, cy), kick, font=f_kick, fill=color)
        y2 = cy + 20
        y2 = draw_lines(d, wrap(d, sh, f_sh, col_w), cx, y2, f_sh, INK, 26)
        draw_lines(d, wrap(d, sb, f_sb, col_w), cx, y2 + 2, f_sb, (40, 40, 40), 20)
        if i % 2 == 0:
            d.line([cx + col_w + 12, cy, cx + col_w + 12, cy + row_h - 8],
                   fill=(200, 198, 190), width=1)
    y += 2 * row_h + 10 + 6
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=2)
    y += 10

    # --- Gaza strip ---
    f_gaza = font(SANS, 17)
    gaza = ("GAZA —  Israeli strike on a truck kills three; Israel's PM-elect "
            "calls West Bank settler arson \u2018Jewish terrorism\u2019.")
    y = draw_lines(d, wrap(d, gaza, f_gaza, INNER), MARGIN, y, f_gaza, INK, 22)
    y += 10

    # --- ticker (black bar, two lines) ---
    f_tick = font(SANS_B, 15)
    tick = ("ALSO TODAY  •  Indonesia factory fire kills 24, dozens missing  •  "
            "Democrats win 258 House seats, largest majority since 1992  •  "
            "Trump signs law retiring the penny; Delta outage delays 1,600 flights")
    tlines = wrap(d, tick, f_tick, INNER - 16)
    th = len(tlines) * 20 + 14
    d.rectangle([MARGIN, y, W - MARGIN, y + th], fill=INK)
    ty = y + 7
    for line in tlines:
        d.text((MARGIN + 8, ty), line, font=f_tick, fill=(255, 255, 255))
        ty += 20
    y += th + 10

    # --- footer ---
    f_foot = font(SANS, 13)
    foot = "All stories reported on 23 November 2026.  Sources: Reuters, The Guardian, NBC News, Just Security."
    d.text(((W - d.textlength(foot, font=f_foot)) / 2, y), foot,
           font=f_foot, fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
