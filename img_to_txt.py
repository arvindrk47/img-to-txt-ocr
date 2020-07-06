import pyfiglet
import pytesseract as tess
from PIL import Image

asc = pyfiglet.figlet_format("Welcome")
print(asc)

ia = pyfiglet.figlet_format("Img To Txt")
print(ia)

print("                        ")
print("                         -DarkArrow")
print("                           ")
print("                           ")
print("                           ")

i = input("Enter the image file:")
img = Image.open(i)
text = tess.image_to_string(img)

print(text)

