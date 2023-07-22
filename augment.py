# This script wasn't used any more as the letter images were small (50x50) 
# The augmentations affected the data 



import os
import Augmentor

SOURCE_DIR = "temp"
p = Augmentor.Pipeline(SOURCE_DIR, save_format="JPEG")

for subdir, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        count = os.path.join(subdir, file)
        print("{} dir number , count : {} ".format(subdir,len(files)))
        val1 = 50 - len(files)
        p.black_and_white(probability=0.8)
        p.sample(val1)
        p.random_distortion(probability=0.6,grid_height=9,grid_width=9,magnitude=1)
        p.sample(val1)
        p.shear(probability=0.8,max_shear_left=5,max_shear_right=5)
        p.sample(20)

