import os
import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    for arg in sys.argv[1:]:
        if os.path.splitext(arg)[1] not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
    if not sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")
    try:
        with Image.open(sys.argv[1]) as before, Image.open("shirt.png").convert("RGBA") as shirt:
            before = ImageOps.fit(before, shirt.size)
            before.paste(shirt, mask=shirt.split()[3])
            before.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")
