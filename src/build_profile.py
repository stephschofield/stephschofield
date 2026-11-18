"""Rebuild the profile SVGs with: python src/build_profile.py

The bitmap font and wave/type animation are adapted from Bakar404/Bakar404.
See THIRD_PARTY_NOTICES.md. No network, packages, secrets, or scheduled jobs.
"""
from pathlib import Path

from pixel import THEMES, Svg, cells_to_path, text_pixels, text_width

ROOT = Path(__file__).resolve().parents[1]
W, M = 846, 423
NAME = "Stephanie Schofield"
GREETING = "I give AI agents jobs. Yes, they get performance reviews."
PROJECTS = [
    ("ecorp", "ECorp",
     "Your 24/7 software factory with all of your human and agent team mates in one digital office.",
     "https://github.com/All-The-Vibes/ecorp"),
    ("atv-bench", "ATV-bench",
     "Benchmark your harness with head-to-head arena matches, ranked by ELO.",
     "https://github.com/All-The-Vibes/ATV-bench"),
    ("atv-starterkit", "ATV-StarterKit",
     "One-click installer that scaffolds a complete GitHub Copilot agentic coding environment into any project. Go.",
     "https://github.com/All-The-Vibes/ATV-StarterKit"),
]
LINKS = [
    ("community", "All The Vibes", "https://github.com/All-The-Vibes"),
    ("linkedin", "LinkedIn", "https://www.linkedin.com/in/stephanieschofield/"),
]

AVATAR = [row.ljust(25, ".") for row in [
    "............ooooo",
    "..........ooHHHHHoo",
    ".........oHHhLLLHHHo",
    "........oHHhLLLLLHHHo",
    "........oHhLLSSSSSHHo",
    "........oHhLSSSSSSSHo",
    "........oHhSSSSSSSSHHo",
    "........oHhSSSSSSSSHHo",
    "........oHhSSSSSSSSHHo",
    "........oHhSSSSSSSSHHo",
    "........oHhSSSRSSSSHHo",
    "........oHhSSSSSSSSHHo",
    "........oHhSSWWWSSSHHo",
    "........oHhSSSRSSSHHHo",
    "........oHHhSSSSSHHHHo",
    "........oHHhHSSSHHHHHo",
    ".......oPPHhHSSSHHHPPo",
    "......oPPPPhHWWWHHPPPPo",
    "......oPPPPHhWWWHHPPPPo",
    ".......oPPPPHhWWPHPPPpPo",
    ".......oPPPPHhWWPHPPPpPo",
    ".......oPPPPHWWWHPPPpPo",
    ".......oPPpPWWWPpPPPpPo",
    ".......oPPpPWWWPpPPPpPo",
    ".......oPPpPWWWPpPPPpPo",
    ".......oPPpPWWWPpPPPpPo",
    ".......oPPpPWWWPpPPSSo",
    ".......oPPpPWWWPpPPSSo",
    ".......oDDDDDDDDDDDSo",
    ".......oDDDDDDDDDDDDo",
    ".......oDDDddDDddDDDo",
    ".......oDDDddoDDddDDo",
    ".......oDDDddoDDddDDo",
    ".......oDDDddoDDddDDo",
    ".......oDDDddoDDddDDo",
    ".......oDDDddoDDddDDo",
    ".......oDDDddoDDddDDo",
    "......oWWWWWo.oWWWWWo",
    "......oWWWWWo.oWWWWWo",
    "......ooooooo.ooooooo",
]]
HANDS = [
    ["...ooo....", "..oSSSo...", "..oSSSo...", "..oSSRSo..", "..oRSRo...",
     "...oPPo...", "...oPPo...", "...oPPo...", "...oPPPo..", "....oPPPo.",
     ".....oPPP.", "......oPP.", ".......oo."],
    [".ooo......", "oSSSo.....", "oSSSo.....", "oSSRSo....", ".oRSRo....",
     "..oPPo....", "..oPPo....", "...oPPo...", "...oPPPo..", "....oPPPo.",
     ".....oPPP.", "......oPP.", ".......oo."],
]
COLOURS = {
    "H": "#a68352", "h": "#c5a773", "L": "#e6ce9e",
    "S": "#f2c7a6", "R": "#c88178", "F": "#544235",
    "W": "#fff9f3", "P": "#e2b9c9", "p": "#bc8fa2",
    "D": "#31394a", "d": "#47516a",
}
AVATAR_PALETTE = {"o": "i", **{key: f"avatar-{key}" for key in COLOURS}}
AVATAR_CSS = "".join(f".avatar-{key}{{fill:{colour}}}" for key, colour in COLOURS.items())
WAVING = [
    "@keyframes wave-l{0%{opacity:1}8.333%{opacity:0}16.667%{opacity:1}25%{opacity:0}"
    "33.333%{opacity:1}41.667%{opacity:0}50%{opacity:1}}",
    "@keyframes wave-r{0%{opacity:0}8.333%{opacity:1}16.667%{opacity:0}25%{opacity:1}"
    "33.333%{opacity:0}41.667%{opacity:1}50%{opacity:0}}",
    "@keyframes lids{0%{opacity:1}72%{opacity:0}75%{opacity:1}}",
]
TYPE = "@keyframes type{from{opacity:0}to{opacity:1}}"
BLINK = "@keyframes blink{50%{opacity:0}}"
PAL = {"#": "i", "p": "p", "Y": "a"}
BOT = [
    ".......##.......", ".......##.......", "..############..", "..#pppppppppp#..",
    ".##pp##pp##pp##.", ".##pp##pp##pp##.", "..#pppppppppp#..", "..#pp######pp#..",
    "..#pppppppppp#..", "..############..", "......####......", "..############..",
    ".#pppppppppppp#.", ".#ppp######ppp#.", ".#pppppppppppp#.", ".##############.",
]
CHIP = [
    "....#..#..#.....", "....#..#..#.....", "..###########...", "..#ppppppppp#...",
    "###ppppppppp###.", "..#pp#pp###p#...", "..#p#p#pp#pp#...", "###p###pp#pp###.",
    "..#p#p#pp#pp#...", "..#p#p#p###p#...", "###ppppppppp###.", "..#ppppppppp#...",
    "..###########...", "....#..#..#.....", "....#..#..#.....", "................",
]
TERMINAL = [
    "................", ".##############.", ".#YYYYYYYYYYYY#.", ".##############.",
    ".#pppppppppppp#.", ".#pp#ppppppppp#.", ".#ppp#pppppppp#.", ".#pppp#ppppppp#.",
    ".#ppp#pppppppp#.", ".#pp#pp####ppp#.", ".#pppppppppppp#.", ".#pppppppppppp#.",
    ".##############.", "................", "................", "................",
]
TV = [
    "....#......#....", ".....#....#.....", "......#..#......", ".##############.",
    ".#pppppppppppp#.", ".#p########ppp#.", ".#p#pppppp#p#p#.", ".#p#pppppp#ppp#.",
    ".#p#pppppp#p#p#.", ".#p#pppppp#ppp#.", ".#p########ppp#.", ".#pppppppppppp#.",
    ".##############.", "....##....##....", "................", "................",
]
INTERESTS = [
    (("Multi-agent evals", "+ reliability"), CHIP),
    (("24/7 software", "factories"), BOT),
    (("Developer tools", "+ harnesses"), TERMINAL),
    (("Silo, Paradise,", "Foundation, GOT"), TV),
]


def canvas(width, height, title, theme):
    return Svg(width, height, title, THEMES["light" if theme == "phone" else theme],
               dark=THEMES["dark"] if theme == "phone" else None)


def notched(x, y, w, h, n=4):
    return (
        f"M{x + 2*n} {y}h{w - 4*n}v{n}h{n}v{n}h{n}v{h - 4*n}h-{n}v{n}h-{n}v{n}"
        f"h-{w - 4*n}v-{n}h-{n}v-{n}h-{n}v-{h - 4*n}h{n}v-{n}h{n}z"
    )


def wrap(text, width, u):
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}" if line else word
        if line and text_width(candidate, u) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    return lines + ([line] if line else [])


def typed(s, text, x, y, u, delay):
    for index, ch in enumerate(text.upper()):
        cells, width = text_pixels(ch)
        at = delay + (index + 1) * 0.045
        s.path(cells_to_path(cells, x, y, u), "i",
               f' style="animation:type {at:.3f}s step-end both"')
        x += (width + 1) * u
    return delay + len(text) * 0.045


def avatar(s, x, y, u):
    s.css.extend([AVATAR_CSS, *WAVING])
    s.sprite(AVATAR, x, y, u, AVATAR_PALETTE)
    for frame, name, opacity in zip(HANDS, ("l", "r"), (1, 0)):
        s.sprite(frame, x, y + 7*u, u, AVATAR_PALETTE,
                 f' style="opacity:{opacity};animation:wave-{name} 4.8s step-end infinite"')
    s.path(cells_to_path([(12, 8), (16, 8)], x, y, u), "avatar-F",
           ' style="animation:lids 4.8s step-end infinite"')


def hero(theme):
    phone = theme == "phone"
    width, u, tu, pad = (M, 3, 2, 14) if phone else (W, 5, 3, 20)
    s = canvas(width, 0, f'{NAME}, waving: "{GREETING}"', theme)
    x = 25*u + (20 if phone else 32)
    if phone:
        first, last = NAME.split()
        s.text(first, 0, 0, 7)
        s.text(last, 0, 70, 7)
        ay, top = 140, 148
    else:
        name_u = min(6, (width - x) // text_width(NAME, 1))
        s.text(NAME, x, 12, name_u)
        ay, top = 8, 78
    lines = wrap(GREETING, width - x - 8 - 2*pad, tu)
    h = 8 + 2*pad + len(lines)*11*tu
    s.path(notched(x, top, width - x, h), "i")
    s.path(notched(x + 4, top + 4, width - x - 8, h - 8), "p")
    s.sprite(["######", ".#pppp", "..#ppp", "...#pp", "....#p", ".....#"],
             x - 20, top + 8, 4, PAL)
    at = 0.6
    s.css.extend([TYPE, BLINK])
    for index, line in enumerate(lines):
        at = typed(s, line, x + 4 + pad, top + 4 + pad + index*11*tu, tu, at)
    s.sprite(["#####", ".###.", "..#.."], width - pad - 5*tu, top + h - pad - 3*tu, tu,
             {"#": "i"}, f' style="animation:type {at:.3f}s step-end both,'
             f'blink 1.06s step-end {at:.3f}s infinite"')
    avatar(s, 0, ay, u)
    s.height = max(ay + len(AVATAR)*u, top + h) + 12
    return s.render()


def heading(theme, title):
    s = canvas(M if theme == "phone" else W, 28, title, theme)
    s.text(title, 0, 8, 2, "m", bold=True)
    return s.render()


def card_text_room(width):
    return width - (144 if width == W else 40)


def project(index, theme):
    width = M if theme == "phone" else W
    _, name, description, _ = PROJECTS[index]
    lines = wrap(description, card_text_room(width), 2)
    tx = 124 if width == W else 20
    h = 68 + len(lines)*24 + 20
    s = canvas(width, h + 16, f"{name}: {description}", theme)
    s.path(notched(0, 0, width, h), "i")
    s.path(notched(4, 4, width - 8, h - 8), "p")
    s.rect(10, 4, width - 20, 42, "a")
    s.text(name, 20, 18, 2, "k", bold=True)
    s.text("→", width - 20, 18, 2, "k", bold=True, anchor="end")
    if width == W:
        s.sprite((BOT, CHIP, TERMINAL)[index], 24, 66, 4, PAL)
    for row, line in enumerate(lines):
        s.text(line, tx, 66 + row*24, 2)
    return s.render()


def interests(theme):
    width, cols = (M, 1) if theme == "phone" else (W, 2)
    title = ("Let's chat about: Multi-agent evals and reliability benchmarks; "
             "24/7 software factories; Developer tools and self-optimizing harnesses; "
             "Silo, Paradise, Foundation, GOT.")
    s = canvas(width, 12 + (4 // cols)*96, title, theme)
    for index, (lines, icon) in enumerate(INTERESTS):
        row, col = divmod(index, cols)
        x, y = col*(width // cols), 12 + row*96
        on, off = index*25, (index + 1)*25
        for name, rest, selected in (
            ("hop", "transform:none", "transform:translateY(-4px)"),
            ("show", "opacity:0", "opacity:1"),
            ("hide", "opacity:1", "opacity:0"),
        ):
            start = f"0%{{{rest}}}" if index else ""
            s.css.append(f"@keyframes {name}{index}{{{start}{on}%{{{selected}}}{off}%{{{rest}}}}}")
        s.add(f'<g style="animation:hop{index} 8s step-end infinite">')
        s.sprite(icon, x, y, 4, PAL, f' style="animation:hide{index} 8s step-end infinite"')
        s.sprite(icon, x, y, 4, {**PAL, "p": "a"},
                 f' style="opacity:0;animation:show{index} 8s step-end infinite"')
        s.add("</g>")
        for row, line in enumerate(lines):
            s.text(line, x + 88, y + 12 + row*24, 2, bold=True)
    return s.render()


def link(label, theme):
    width = (M if theme == "phone" else W) // 2
    s = canvas(width, 76, label, theme)
    s.path(notched(4, 8, width - 8, 60), "i")
    s.path(notched(8, 12, width - 16, 52, 3), "o")
    s.path(notched(8, 12, width - 16, 44, 3), "a")
    s.text(label, width // 2, 27, 2, "k", bold=True, anchor="middle")
    return s.render()


def assets():
    result = {}
    for theme in ("light", "dark", "phone"):
        result[f"hero-{theme}.svg"] = hero(theme)
        result[f"projects-{theme}.svg"] = heading(theme, "Currently focused on")
        result[f"interests-heading-{theme}.svg"] = heading(theme, "Let's chat about")
        result[f"interests-{theme}.svg"] = interests(theme)
        for index, (slug, *_) in enumerate(PROJECTS):
            result[f"project-{slug}-{theme}.svg"] = project(index, theme)
        for slug, label, _ in LINKS:
            result[f"link-{slug}-{theme}.svg"] = link(label, theme)
    return result


if __name__ == "__main__":
    (ROOT / "assets").mkdir(exist_ok=True)
    for name, svg in assets().items():
        (ROOT / "assets" / name).write_text(svg, encoding="utf-8", newline="\n")
    print("Built 27 profile SVGs.")
