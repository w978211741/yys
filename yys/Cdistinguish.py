import pytesseract
from PIL import Image


class Distinguish:

    @staticmethod
    def img_path2string(img):
        text = pytesseract.image_to_string(Image.open(img))
        return text

    @staticmethod
    def img2string(img):
        text = pytesseract.image_to_string(img, lang='eng')
        return text

