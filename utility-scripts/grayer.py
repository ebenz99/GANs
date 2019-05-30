from __future__ import absolute_import, division, print_function

import tensorflow as tf
import os
import pathlib
data_root = os.getcwd()+"/database"
data_root = pathlib.Path(data_root)
import random
from skimage.io import *
from skimage import *

all_image_paths = list(data_root.glob('*'))
all_image_paths = [str(path) for path in all_image_paths]
random.shuffle(all_image_paths)

image_count = len(all_image_paths)
image_count

import IPython.display as display


from matplotlib import pyplot as plt
from PIL import Image


for impath in all_image_paths:
	print(impath)
	fname = os.path.split(impath)
	image = imread(impath)
	image = color.rgb2gray(image)
	imsave(impath, image)
	print()

