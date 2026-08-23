from pathlib import Path

lines = [
    ("Parth Bathla", ""),
    ("────────────────────────", ""),
    ("Now", "Computer Science Student"),
    ("Stack", "Java • Python • HTML/CSS • MySQL"),
    ("Learning", "DSA • AI • Web Development"),
    ("Projects", "AI + IoT • Web Applications"),
    ("GitHub", "bathlaparth036-max"),
]

svg_lines = []

y = 50

for i, (key, value) in enumerate(lines):
    text = key if not value else f"{key}: {value}"

    svg_lines.append(f'''
    <text x="30" y="{y}"
          class="line"
          style="animation-delay:{i * 0.5}s">
        {text}
    </text>
    ''')

    y += 42

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="600" height="360"
    viewBox="0 0 600 360">

<style>
    svg {{
        background: #0d1117;
    }}

    .line {{
        fill: #c9d1d9;
        font-family: monospace;
        font-size: 20px;
        opacity: 0;
        animation: show 0.5s forwards;
    }}

    @keyframes show {{
        from {{
            opacity: 0;
            transform: translateX(-15px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
</style>

<rect width="100%" height="100%" rx="15"
      fill="#0d1117"
      stroke="#30363d"
      stroke-width="2"/>

{''.join(svg_lines)}

</svg>
'''

Path("info-card.svg").write_text(svg, encoding="utf-8")

print("Info card created successfully!")