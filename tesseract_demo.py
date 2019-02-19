# 使用pytesseract将图片上的文字转换为文本文字

import pytesseract
from PIL import Image

# 指定tesseract的路径
pytesseract.pytesseract.tesseract_cmd = r"G:\ProgramApp\TesseractOCR\tesseract.exe"

# 打开图片
image_en = Image.open('test_a.png')
# image_zh = Image.open('')

# 调用image_to_string将图片转换为文字
text_en = pytesseract.image_to_string(image_en)
# text_zh = pytesseract.image_to_string(image_zh,lang='chi_sim')
print(text_en)
print('='*60)
# print(text_zh)
