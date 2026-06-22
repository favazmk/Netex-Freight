from PIL import Image
import vtracer
import os

def remove_white_bg(image_path, out_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Check if the pixel is white or very close to white
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0)) # transparent
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(out_path, "PNG")

print("Processing favicon...")
remove_white_bg("favicon.png", "favicon-transparent.png")
vtracer.convert_image_to_svg_py(
    "favicon-transparent.png",
    "favicon.svg",
    colormode='color',
    hierarchical='stacked',
    mode='spline',
    color_precision=8,
    layer_difference=16,
    corner_threshold=60,
    length_threshold=4.0,
    max_iterations=10,
    splice_threshold=45,
    path_precision=8
)

print("Processing logo-cropped...")
remove_white_bg("logo-cropped.png", "logo-cropped-transparent.png")
vtracer.convert_image_to_svg_py(
    "logo-cropped-transparent.png",
    "logo-cropped.svg",
    colormode='color',
    hierarchical='stacked',
    mode='spline',
    color_precision=8,
    layer_difference=16,
    corner_threshold=60,
    length_threshold=4.0,
    max_iterations=10,
    splice_threshold=45,
    path_precision=8
)

print("Done!")
