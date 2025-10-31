import os
import random

output_dir = 'src/data'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'generated_img.svg')

svg_width, svg_height = 400, 400
num_circles = 10

svg_elements = []
for _ in range(num_circles):
    cx = random.randint(0, svg_width)
    cy = random.randint(0, svg_height)
    r = random.randint(10, 50)
    color = f'rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})'
    svg_elements.append(
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" />'
    )

svg_content = f'''<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
{chr(10).join(svg_elements)}
</svg>
'''

with open(output_path, 'w') as f:
    f.write(svg_content)