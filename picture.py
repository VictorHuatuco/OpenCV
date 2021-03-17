from PIL import Image
import pytesseract

img = Image.open('picture.png')
text = pytesseract.image_to_string(img)
print(text)
