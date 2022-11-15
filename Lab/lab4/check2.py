import check2_helper

from PIL import Image


im = Image.open('im.jpg')

im1 = Image.open('ca.jpg')

im2 = Image.open('hk.jpg')

im3 = Image.open('bw.jpg')

'''Creating a blank new image'''

newim = Image.new('RGB', (512, 512), 'white')


im4 = check2_helper.make_square(im)
newim.paste(im4,(0,0))

im5 = check2_helper.make_square(im1)
newim.paste(im5,(0,256))

im6 = check2_helper.make_square(im2)
newim.paste(im6,(256,0))

im7 = check2_helper.make_square(im3)
newim.paste(im7,(256,256))

newim.show()



'''im4 = im.resize((256,256))
newim.paste(im4, (0,0))

im5 = im1.resize((256,256))
newim.paste(im5, (0,256))

im6 = im2.resize((256,256))
newim.paste(im6, (256,0))

im7 = im3.resize((256,256))
newim.paste(im7, (256,256))

newim.show()'''