from PIL import Image

def bilde():
    datne = 'Images/bilde.jpg'
    with Image.open(datne) as im:

        print(datne, im.format, f"{im.size}x{im.mode}")
        im.show()
        izmers = (100, 100)
        im.thumbnail(izmers)
        im.save("Images/bilde-maza.jpg", im.format)
        im.show()
bilde()

def pagriezt(nosaukums):
    with Image.open(f'Images/{nosaukums}') as img:
        img = img.rotate(90)
        img.save(f'Images/cits-{nosaukums}', img.format)

pagriezt('cj.jpg')

def sikatels(name,pikseli):
    izmers = pikseli.split(',')
    x = int(izmers[0])
    y = int(izmers[1])
    izmeers = (x,y)
    with Image.open(f'Images/{name}') as image:
        image.thumbnail(izmeers)
        image.save(f'Images/Izmainits_{name}', image.format)

sikatels('cj.jpg','100,100')
