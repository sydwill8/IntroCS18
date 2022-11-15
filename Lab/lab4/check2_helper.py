''' Program crops an image into a square'''

'''Author: Sydnee Williams'''

from PIL import Image


def make_square(im):
    w,l = im.size
    if w > l:
        newim = im.crop((w // 4, l // 6 , l, l))
    if l > w:
        newim = im.crop((w // 4, l // 6, w, w))
    return newim