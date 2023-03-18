'''
import cv2
import os

IMG_DIR = './train_data'


def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            resized = cv2.resize(img, (64, 64))
            cv2.imwrite('./resize_data/' + filename, resized)


load_images_from_folder(IMG_DIR)
'''