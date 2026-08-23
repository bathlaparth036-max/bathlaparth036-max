from PIL import Image
import html

INPUT = "source-prepped.png"
OUTPUT = "avi-ascii.svg"

# Bright to dark characters
RAMP = " .`:-=+*cs#%@"

WIDTH = 90
HEIGHT = 50

image = Image.open(INPUT).convert("L")

image = image.resize((WIDTH, HEIGHT))

pixels = image.load()

rows = []

for y in range(HEIGHT):

    row = ""

    for x in range(WIDTH):

        brightness = pixels[x, y]

        index = int(
            brightness / 256 * len(RAMP)
        )

        index = min(index, len(RAMP) - 1)

        row += RAMP[index]

    rows.append(row)


svg_width = 750
svg_height = 650

font_size = 11
line_height = 12

svg = []

svg.append(f'''
<svg xmlns="http://www.w3.org/2000/svg"
width="{svg_width}"
height="{svg_height}"
viewBox="0 0 {svg_width} {svg_height}">

<rect width="100%" height="100%" fill="#0d1117"/>

<style>
.text {{
    font-family: monospace;
    font-size: {font_size}px;
    fill: #d0d7de;
}}
</style>
''')

for i, row in enumerate(rows):

    y = 30 + i * line_height

    escaped = html.escape(row)

    delay = i * 0.08

    svg.append(f'''

<clipPath id="clip{i}">
    <rect
        x="20"
        y="{y-font_size}"
        width="0"
        height="{line_height}">

        <animate
            attributeName="width"
            from="0"
            to="700"
            begin="{delay}s"
            dur="0.4s"
            fill="freeze"
        />
    </rect>
</clipPath>

<text
    x="20"
    y="{y}"
    class="text"
    clip-path="url(#clip{i})">

    {escaped}

</text>
''')

svg.append("</svg>")

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as file:

    file.write("\n".join(svg))

print("ASCII portrait created!")