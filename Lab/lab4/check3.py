

import check2_helper

from PIL import Image


im = Image.open('1.jpg')

im1 = Image.open('2.jpg')

im2 = Image.open('3.jpg')

im3 = Image.open('4.jpg')

im4 = Image.open('5.jpg')

im5 = Image.open('6.jpg')

'''Creating a blank new image'''

newim = Image.new('RGB', (1000, 360))


w,l = im.size
im6 = im.resize((round(((w/l) *256)),256))
newim.paste(im6, (31, 20))

w,l = 0,0
w,l = im1.size
w_6, h = im6.size
im7 = im1.resize((round((w/l) * 256), 256))
newim.paste(im7, ((w_6 + 41, 60)))


w,l = 0,0
new_w = w_6 + 41
w,l = im2.size
w_7, h = im7.size
im8 = im2.resize((round((w/l) * 256), 256))
newim.paste(im8, ((new_w + w_7 + 10), 20))


w,l = 0, 0
new_w1 = new_w + w_7 + 10
w,l = im3.size
w_8, h = im8.size
im9 = im3.resize((round((w/l) * 256), 256))
newim.paste(im9, (new_w1 + w_8 + 10, 60))


w,l = 0,0
new_w2 = new_w1 + w_8 + 10
w,l = im4.size
w_9, h = im9.size
im10 = im4.resize((round((w/l) * 256), 256))
newim.paste(im10, (new_w2 + w_9 + 10, 20))

w,l = 0,0
new_w3 = new_w2 + w_9 + 10
w,l = im5.size
w_10, h = im10.size
im11 = im5.resize((round((w/l) * 256), 256))
newim.paste(im11, (new_w3 + w_10 + 10, 60))
newim.show()
