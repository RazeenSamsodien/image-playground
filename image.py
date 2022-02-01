from PIL import Image, ImageFilter

#img = Image.open('./Pokedex/203 pikachu.jpg')
#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img.save("grey.png", 'png')
#filtered_img = img.convert('L')

#crooked = filtered_img.rotate(90)
#crooked.save("crooked and grey", 'png')

#resize = filtered_img.resize((300, 300))
#resize.save("resized grey.png", 'png')

img = Image.open('examples/astronaut.jpg')
#new_img = img.resize((400,200))
#new_img.save('thumbnail.jpg')

img.thumbnail((400,400))
img.save('thumbnail2.jpg')
print(img.size)
