from PIL import Image, ImageDraw, ImageFilter

# 알고리즘 순서
# 1. 옷 이미지의 크기를 아바타 이미지의 크기의 비율에 맞게 줄인다.
# 2. 옷 이미지와 아바타 이미지를 RGBA 형식으로 변환한다.
# 3. (아바타 이미지 너비 - 옷 이미지 너비) / 2 를 하여 절대적 x축 값을 구한다.
# 4. 아바타 이미지에 옷 이미지를 넣는다.

def paste_man():
    # Stage 1
    # women/women60.png
    im1 = Image.open("./static/betterfit/images/men/man80.png") # 500x530
    im2 = Image.open("./output/output2.png") # 768x1152

    half = 0.3
    im2 = im2.resize( [int(half * s) for s in im2.size] )

    # Convert image to RGBA
    im1 = im1.convert("RGBA")

    # Convert image to RGBA
    im2 = im2.convert("RGBA")

    # Calculate width to be at the center
    width = (im1.width - im2.width) // 2

    # Calculate height to be at the center
    #height = (im1.height - im2.height) // 2

    # Paste the frontImage at (width, height)
    im1.paste(im2, (width, 120), im2)

    # Save this image
    im1.save("./model_img/model.png", format="png")

    # Stage 2
    im3 = Image.open("./model_img/model.png")
    im4 = Image.open("./output/output1.png") # 768x1152

    half = 0.3
    im4 = im4.resize( [int(half * s) for s in im4.size] )

    # Convert image to RGBA
    im3 = im3.convert("RGBA")

    # Convert image to RGBA
    im4 = im4.convert("RGBA")

    # Calculate width to be at the center
    width = (im3.width - im4.width) // 2

    # Paste the frontImage at (width, height)
    im3.paste(im4, (width, -50), im4)

    # Save this image
    im3.save("./model_img/model_final.png", format="png")

    print('Successful')

#paste_man()
