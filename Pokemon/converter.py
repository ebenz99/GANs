from PIL import Image
import numpy as np
import os, sys 

def load_image(infilename) :
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

def save_image( npdata, outfilename ) :
    img = Image.fromarray(np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L")
    img.save(outfilename)

path = os.getcwd()+"/database/" 
dirs = os.listdir(path) 

#443 x 80 x 100
training_data = np.ndarray(shape=(819,128,128,4), dtype = "float")


for idx,item in enumerate(dirs): 
	a = load_image(path+item)
	print(type(a))
	print(a.shape)
	training_data[idx] = a


print(training_data[400][22][90])
print(training_data[300][70][2])

np.save(os.getcwd()+"/pickles/train_data.npy", training_data)