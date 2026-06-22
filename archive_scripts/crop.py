from PIL import Image, ImageChops

def trim(im_path, out_path):
    im = Image.open(im_path).convert("RGBA")
    
    # Try alpha bounding box first
    alpha = im.getchannel('A')
    bbox = alpha.getbbox()
    
    # If the whole image is opaque, or near opaque, try cropping white space
    if bbox == (0, 0, im.width, im.height) or bbox is None:
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        
    if bbox:
        im = im.crop(bbox)
        
    im.save(out_path)

trim("Netex final logo.PNG", "logo-cropped.png")
