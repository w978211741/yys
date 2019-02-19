import pytesseract
from PIL import Image

class cdisdigit:

    def imgPathtostring(self,img):
        text = pytesseract.image_to_string(Image.open(img))
        return text

    def imgtostring(self,img):
        text = pytesseract.image_to_string(img,lang='eng')
        return text