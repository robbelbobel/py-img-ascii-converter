from PIL import Image
import sys

density = ['Ñ', '@', '#', 'W', '$', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '?', '!', 'a', 'b', 'c', ';', ':', '+', '=', '-', ',', '.', '_', ' ']

density.reverse()

def calculate_pixel_density(img, x, y):
    pixeldata = img.getpixel((x, y))
    return int(((float(pixeldata[0] + pixeldata[1] + pixeldata[2]) / 3) / 256) * 29)

if len(sys.argv) != 2:
    print("ERROR: Invalid argument count!")
    exit()

img = Image.open(sys.argv[1])
res_file = open("res.txt", 'w')

for i in range(0, img.height):
    for j in range(0, img.width):
        res_file.write(density[(calculate_pixel_density(img, j, i))])
        pass
    res_file.write("\n")
    print(str((i * 100) // img.height) + "%")

res_file.close()

print("Finished. Refer to the res.txt file for the result.")