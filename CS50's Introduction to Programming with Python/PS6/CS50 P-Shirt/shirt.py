import sys
from PIL import Image, ImageOps

if len(sys.argv) < 2:
    sys.exit("Too few arguments!")
elif len(sys.argv) >2:
    sys.exit("Too many arguments!")


if not sys.argv[1].endswith(".jpg"):
    sys.exit("Not a jpg file!")
else:
    try:
        image1 = Image.open(sys.argv[1]).convert("RGBA")

        width, height = image1.size

        image2 = ImageOps.fit(image1, (600, 600), method=Image.LANCZOS, centering=(0.5, 0))

        shirt = Image.open("shirt.png").convert("RGBA")

        image2.paste(shirt, shirt)

        image2 = image2.convert("RGB")

        image2.save("after.jpg")
    except FileNotFoundError:
        sys.exit("File does not exist!")