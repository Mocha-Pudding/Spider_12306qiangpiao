# 用pytesseract处理拉勾网图形验证码：

import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r"G:\ProgramApp\TesseractOCR\tesseract.exe"
    url = ''
    while True:
        request.urlretrieve(url,'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)

if __name__ == '__main__':
    main()