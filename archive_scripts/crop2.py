from PIL import Image, ImageChops

def trim(im_path, out_path, tolerance=30):
    im = Image.open(im_path).convert("RGBA")
    
    bg_color = im.getpixel((0, 0))
    bg = Image.new("RGBA", im.size, bg_color)
    
    diff = ImageChops.difference(im, bg)
    
    diff = diff.convert("L")
    diff = diff.point(lambda p: 255 if p > tolerance else 0)
    
    bbox = diff.getbbox()
    
    if bbox:
        x1, y1, x2, y2 = bbox
        x1 = max(0, x1 - 10)
        y1 = max(0, y1 - 10)
        x2 = min(im.width, x2 + 10)
        y2 = min(im.height, y2 + 10)
        im = im.crop((x1, y1, x2, y2))
        print(f"Cropped size: {im.size}")
    else:
        print("No crop needed or found")
        
    im.save(out_path)

trim("Netex final logo.PNG", "logo-cropped.png")
