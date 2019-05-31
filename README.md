# GANs

## Image Utility Scripts

First things first, if you're doing ML, you're probably going to need a training dataset of some kind. Because I'm probably not capable of making a GAN work with anything more than images, I made/adapted a bunch of scripts to take care of the dirty work for images I've found online.

`grayer.py` - converts all images in target directory to grayscale images (single-channel). This isn't exactly necessary but makes things nicer for the learning part

`resizer.py` - resizes all images in a target directory to specified dimensions. Usually, unless you've got a ton of time and resources, smaller input images ~= more desireable

`converter.py` - saves all images from target directory into a numpy ndarray in memory

## NBA-headshots

Pretty straightforward. Credit to github user @mroeschke for getting every NBA player headshot from 2015-2016 somehow. All that was needed for prepping them was making them mono-channel and resizing them so the input layer wasn't large enough to slow things down too much. At around epoch 2400, a more defined headshot silhouette begins to take shape.

## Pokemon

This should be more of a challenge for the GAN, as I'm going from mono-channel to four-channel data