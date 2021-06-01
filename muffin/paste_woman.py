from PIL import Image, ImageDraw, ImageFilter

def paste_woman():
    # Stage 1
    # men/man80.png
    im3 = Image.open("./static/betterfit/images/women/women60.png") # 500x530
    im4 = Image.open("./output/output3.png") # 768x1152

    half = 0.3
    im4 = im4.resize( [int(half * s) for s in im4.size] )

    # Convert image to RGBA
    im3 = im3.convert("RGBA")

    # Convert image to RGBA
    im4 = im4.convert("RGBA")

    # Calculate width to be at the center
    width = (im3.width - im4.width) // 2

    # Paste the frontImage at (width, height)
    im3.paste(im4, (width, -8), im4)

    # Save this image
    im3.save("./model_img/model_final2.png", format="png")

    print('Successful')

#paste_woman()
