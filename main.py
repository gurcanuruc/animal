import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from gui import *

data_dir = "C:/Users/Emrehan Metin/Desktop/Metin/image"

class_names = os.listdir(data_dir)  #program indirdigim dataseti goruyor mu onu test ettim 
print("Classes: ", class_names)

sample_image_path = os.path.join(data_dir, class_names[0], os.listdir(os.path.join(data_dir, class_names[0]))[1])
sample_image = plt.imread(sample_image_path)
plt.imshow(sample_image)
plt.title(f"CLASS: {class_names[0]}")
plt.show() #goruyormus