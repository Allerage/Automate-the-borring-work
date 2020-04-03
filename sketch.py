import imageio
import numpy as np
import matplotlib.pyplot as p
from scipy import ndimage


def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def dodge(front, back):
    result = front*255/(255-back)
    result[result > 255] = 255

    result[back == 255] = 255
    return result.astype('uint8')


img = r"C:\Users\Allerage\Desktop\livro\test.jpg"
s_img = imageio.imread(img)
# start_img.shape(196, 160, 30)
gray_img = grayscale(s_img)
inverted_img = 255 - gray_img
blur_img = ndimage.filters.gaussian_filter(inverted_img, sigma=5)
final_img = dodge(blur_img, gray_img)
p.imshow(final_img, cmap='gray')
p.imsave(r"C:\Users\Allerage\Desktop\livro\test1.jpg",
         final_img, cmap='gray', vmin=0, vmax=255)
