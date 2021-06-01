from rembg.bg import remove
import numpy as np
import io
import os
import glob
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
lenI = 0

# jpg/jpeg 등의 사진 파일을 png 형식으로 변환해주는 코드
def topng():
    image_files = os.listdir("./media")
    file_ext = ".png"
    global x
    x = 0

    matching = [s for s in image_files if "input" in s]
    image_files = list(set(image_files) - set(matching))
    lenI = len(matching)

    if not image_files:
        print("This folder is empty")
    else:
        for filename in image_files:
                x += 1
                filepath = os.path.join("./media",filename)
                new_filepath = os.path.join("./media","input{0}{1}".format(x + lenI, file_ext))
                os.rename(filepath, new_filepath)
        print("File names have been changed")

def removebackground():
    input_path = glob.glob("./media" + "/**/*.png", recursive = True)
    global y
    y = 1

    # input 이미지 삽입
    for i in range(len(input_path)):
        f = np.fromfile(input_path[i+lenI])
        # input 이미지 배경 제거
        result = remove(f)
        # 배경 제거한 이미지 변환
        img = Image.open(io.BytesIO(result)).convert("RGBA")
        # 이미지 저장
        img.save('./output/output' + str(y+lenI) + '.png')
        y += 1

#if __name__ == '__main__':
#    topng()
#    removebackground()
