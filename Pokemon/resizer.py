from PIL import Image 
import os, sys 
path = os.getcwd()+"/database/" 
dirs = os.listdir( path ) 

def resize(): 
   for item in dirs: 
      im = Image.open(path+item) 
      f, e = os.path.splitext(path+item) 
      print(f)
      print(e)
      imResize = im.resize((128,128), Image.ANTIALIAS) 
      imResize.save(f + e, 'PNG', quality=90) 

resize()