"""Draws how a change ships at SINCPRO today, once per GitHub theme: five steps, who does
each one, and production feeding back into the next spec.

usage: python3 loop_svg.py <out_dir>
"""

import sys
from pathlib import Path

THEMES = {
    "light": {"primary": "#1f2328", "secondary": "#59636e", "label": "#818b98",
              "box": "#f6f8fa", "border": "#d1d9e0", "accent": "#8250df", "page": "#ffffff"},
    "dark": {"primary": "#f0f6fc", "secondary": "#9198a1", "label": "#656c76",
             "box": "#151b23", "border": "#3d444d", "accent": "#ab7df8", "page": "#0d1117"},
}

# who, step, two lines on what happens; the agent's step is the only one a person does not do
STEPS = [
    ("FUNCTIONAL TEAM", "Spec", ("What the process needs,", "written by who knows it")),
    ("AI AGENT", "Build", ("Written in a sandbox,", "inside our framework")),
    ("ENGINEERS", "Review", ("Checks, then a review", "of the architecture")),
    ("FUNCTIONAL TEAM", "Preview", ("Each pull request gets", "its own environment")),
    ("PLATFORM", "Production", ("Kubernetes, 86+ clients,", "observed end to end")),
]

WIDTH, GAP = 860, 26
BOX_W = (WIDTH - GAP * (len(STEPS) - 1)) / len(STEPS)
BOX_Y, BOX_H = 4, 100
RETURN_Y = BOX_Y + BOX_H + 30
HEIGHT = RETURN_Y + 14
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"


def left(index: int) -> float:
    return round(index * (BOX_W + GAP), 1)


def middle(index: int) -> float:
    return round(left(index) + BOX_W / 2, 1)


def draw(theme: dict[str, str]) -> str:
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" '
        'aria-label="Spec, build, review, preview, production, and back to the spec">',
        "<defs>",
        f'<marker id="head" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">'
        f'<path d="M0,0 L8,4 L0,8 z" fill="{theme["label"]}"/></marker>',
        "</defs>",
        f'<g font-family="{FONT}">',
    ]

    for index, (who, step, (line1, line2)) in enumerate(STEPS):
        x, mid = left(index), middle(index)
        agent = who == "AI AGENT"
        parts += [
            f'<rect x="{x + 0.75}" y="{BOX_Y}" width="{round(BOX_W - 1.5, 1)}" height="{BOX_H}" rx="10" '
            f'fill="{theme["box"]}" stroke="{theme["accent"] if agent else theme["border"]}" '
            f'stroke-width="{1.5 if agent else 1}"/>',
            f'<text x="{mid}" y="{BOX_Y + 22}" font-size="9.5" font-weight="600" letter-spacing="1" '
            f'text-anchor="middle" fill="{theme["accent"]}">{who}</text>',
            f'<text x="{mid}" y="{BOX_Y + 48}" font-size="15" font-weight="600" text-anchor="middle" '
            f'fill="{theme["primary"]}">{step}</text>',
            f'<text x="{mid}" y="{BOX_Y + 70}" font-size="11" text-anchor="middle" fill="{theme["secondary"]}">{line1}</text>',
            f'<text x="{mid}" y="{BOX_Y + 85}" font-size="11" text-anchor="middle" fill="{theme["secondary"]}">{line2}</text>',
        ]
        if index < len(STEPS) - 1:
            start, end = round(x + BOX_W + 4, 1), round(left(index + 1) - 4, 1)
            y = BOX_Y + BOX_H / 2
            parts.append(
                f'<line x1="{start}" y1="{y}" x2="{end}" y2="{y}" stroke="{theme["label"]}" '
                'stroke-width="1.5" marker-end="url(#head)"/>'
            )

    first, last = middle(0), middle(len(STEPS) - 1)
    bottom = BOX_Y + BOX_H
    label = "errors and traces go back into the next spec"
    parts += [
        f'<path d="M{last},{bottom + 3} V{RETURN_Y - 8} Q{last},{RETURN_Y} {last - 8},{RETURN_Y} '
        f'H{first + 8} Q{first},{RETURN_Y} {first},{RETURN_Y - 8} V{bottom + 5}" fill="none" '
        f'stroke="{theme["label"]}" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#head)"/>',
        f'<rect x="{WIDTH / 2 - 150}" y="{RETURN_Y - 9}" width="300" height="18" fill="{theme["page"]}"/>',
        f'<text x="{WIDTH / 2}" y="{RETURN_Y + 4}" font-size="12" font-style="italic" text-anchor="middle" '
        f'fill="{theme["secondary"]}">{label}</text>',
        "</g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (out / f"loop-{name}.svg").write_text(draw(theme), encoding="utf-8")


if __name__ == "__main__":
    main()
