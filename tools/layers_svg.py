"""Draws the profile's layers chart, once per GitHub theme: each layer starts in its year, is
thick while it was the main work and stays thin afterwards, so the right edge shows them all.

usage: python3 layers_svg.py <out_dir>
"""

import sys
from pathlib import Path

THEMES = {
    "light": {"primary": "#1f2328", "secondary": "#59636e", "label": "#818b98",
              "grid": "#d1d9e0", "accent": "#8250df"},
    "dark": {"primary": "#f0f6fc", "secondary": "#9198a1", "label": "#656c76",
             "grid": "#3d444d", "accent": "#ab7df8"},
}

NOW = 2026.87
# name, evidence, starts, main work until (None: still the main work)
LAYERS = [
    ("Full-stack web on Linux", "Boxit · Key Work ERP", 2017.0, 2018.6),
    ("Services, DDD and CQRS", "Expresa Tech · ScienceLogic", 2018.6, 2021.9),
    ("Kubernetes and observability", "SINCPRO · 86+ clients in production", 2021.0, None),
    ("Business process and ERP", "Odoo functional · ISO 9001", 2021.0, None),
    ("Cloud services and data", "Aetion · Electric", 2022.0, 2025.6),
    ("AI-driven delivery", "Forge · MCP servers · frameworks", 2025.0, None),
]

WIDTH = 860
CHART_X0, YEAR_PX, FIRST_YEAR = 272, 55, 2017
TOP, ROW = 8, 38
AXIS_Y = TOP + ROW * len(LAYERS) + 8
HEIGHT = AXIS_Y + 26
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"


def x(year: float) -> float:
    return round(CHART_X0 + (year - FIRST_YEAR) * YEAR_PX, 1)


def row_y(index: int) -> float:
    """Oldest layer at the bottom: each new one is stacked on top."""
    return TOP + ROW * (len(LAYERS) - 1 - index) + ROW / 2


def draw(theme: dict[str, str]) -> str:
    now = x(NOW)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" '
        'aria-label="Six layers of work, each added on top of the last, all still in use today">',
        f'<g font-family="{FONT}">',
    ]

    for year in (2017, 2019, 2021, 2023, 2025):
        parts += [
            f'<line x1="{x(year)}" y1="{TOP}" x2="{x(year)}" y2="{AXIS_Y}" stroke="{theme["grid"]}" '
            'stroke-width="1" stroke-dasharray="2 4"/>',
            f'<text x="{x(year)}" y="{AXIS_Y + 18}" font-size="11.5" text-anchor="middle" '
            f'fill="{theme["label"]}">{year}</text>',
        ]
    parts += [
        f'<line x1="{now}" y1="{TOP}" x2="{now}" y2="{AXIS_Y}" stroke="{theme["accent"]}" '
        'stroke-width="1.5" stroke-opacity="0.6"/>',
        f'<text x="{now}" y="{AXIS_Y + 18}" font-size="11.5" font-weight="600" text-anchor="middle" '
        f'fill="{theme["accent"]}">now</text>',
    ]

    for index, (name, evidence, starts, main_until) in enumerate(LAYERS):
        y = row_y(index)
        main_end = x(main_until if main_until is not None else NOW)
        parts += [
            f'<text x="0" y="{y - 2}" font-size="13.5" font-weight="600" fill="{theme["primary"]}">{name}</text>',
            f'<text x="0" y="{y + 14}" font-size="11.5" fill="{theme["secondary"]}">{evidence}</text>',
            f'<rect x="{x(starts)}" y="{y - 5}" width="{round(main_end - x(starts), 1)}" height="10" rx="5" '
            f'fill="{theme["accent"]}"/>',
        ]
        if main_until is not None:
            parts.append(
                f'<rect x="{main_end - 4}" y="{y - 1.5}" width="{round(now - main_end + 4, 1)}" height="3" '
                f'rx="1.5" fill="{theme["accent"]}" fill-opacity="0.35"/>'
            )

    parts += ["</g>", "</svg>", ""]
    return "\n".join(parts)


def main() -> None:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (out / f"layers-{name}.svg").write_text(draw(theme), encoding="utf-8")


if __name__ == "__main__":
    main()
