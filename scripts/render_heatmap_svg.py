import json
from datetime import datetime
from pathlib import Path

with open("data/contributions.json") as f:
    data = json.load(f)

days = data["days"]

CELL = 14
GAP = 4

PALETTE = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

svg_parts = []

for i, day in enumerate(days):

    week = i // 7
    weekday = i % 7

    x = 40 + week * (CELL + GAP)
    y = 40 + weekday * (CELL + GAP)

    level = min(day["level"], 4)

    delay = i * 0.01

    svg_parts.append(f'''
    <rect
        x="{x}"
        y="{y}"
        width="{CELL}"
        height="{CELL}"
        rx="3"
        fill="{PALETTE[level]}"
        class="cell"
        style="animation-delay:{delay}s"
    />
    ''')

width = 40 + 53 * (CELL + GAP)
height = 220

svg = f'''
<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}"
     height="{height}">

<style>
.cell {{
    opacity: 0;
    animation: reveal 0.4s forwards;
}}

@keyframes reveal {{
    from {{
        opacity: 0;
        transform: translateY(-10px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

text {{
    fill: #8b949e;
    font-family: monospace;
}}
</style>

<rect width="100%" height="100%"
      fill="#0d1117"
      rx="12"/>

<text x="40" y="25">
{data["username"]}'s Contributions
</text>

{''.join(svg_parts)}

</svg>
'''

Path("contrib-heatmap.svg").write_text(svg)

print("Contribution heatmap created successfully!")