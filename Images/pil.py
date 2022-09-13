from PIL import Image

# DoggieImage = Image.open('Doggie.jpg')
# DoggieImage.load()

try:
    DoggieImage = Image.open('Images\Doggie.jpg')
except FileNotFoundError:
    print('File Not Found!')
DoggieImage.load()

print(DoggieImage.format, DoggieImage.size, DoggieImage.mode)
DoggieImage.show()