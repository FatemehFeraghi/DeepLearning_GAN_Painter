import os
import numpy as np
from PIL import Image

IMAGE_SIZE = 128
IMAGE_CHANNELS = 3
IMAGE_DIR = 'images/Cubism'

from tqdm import tqdm

images_path = IMAGE_DIR

training_data = []

print('resizing')

try:
    for filename in tqdm(os.listdir(images_path)):
        path = os .path.join(images_path , filename)
        if os.stat(path).st_size == 3227:
             pass
        else:
            im = Image.open(path)
            image = im.convert('RGB')
            image = image.resize(
                  (IMAGE_SIZE, IMAGE_SIZE)
                )
            training_data.append(np.asarray(image))


except:
    pass

training_data = np.reshape(
    training_data, (-1, IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNELS))
training_data = training_data / 127.5 - 1

print('Saving file....')
np.save('training_data.npy')
