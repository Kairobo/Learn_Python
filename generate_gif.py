import imageio
import os
image_dir = './pre-output1/'

tm_list = os.listdir(image_dir)

#tm_list = sorted(tm_list, key=lambda x: int(x.split('image')[1].split('-')[0]))
#img_list.append(tm_list)
images = []

for filename in tm_list:
    img_dir = image_dir + filename
    print(img_dir)
    images.append(imageio.imread(img_dir))
imageio.mimsave('./movie.gif', images)