# -*- coding:utf8 -*-

import os
import cv2
import imageio
import numpy as np
from glob import glob


def show_picture(filename="timg.jpeg", m=50):
    data = cv2.imread(filename)
    n_chanal = data.shape[-1]
    new_data = []
    for i in range(n_chanal):
        u, s, v = np.linalg.svd(data[:,:,i])
        for j in range(s.shape[0]):
            if j >= m: s[j] = 0.0
        s = np.diag(s)
        s = np.concatenate((s, np.zeros(shape=(s.shape[0], v.shape[0]-s.shape[0]))), axis=1)
        new_data.append(np.dot(np.dot(u, s), v)[:,:,np.newaxis])
    new_data = np.concatenate(new_data, axis=-1)
    if not os.path.exists("timg_svds"):
        os.makedirs("timg_svds")
    cv2.imwrite('timg_svds/svd-{}.jpeg'.format(m),new_data)


def show_gif(filepattern="timg_svds/*.jpeg"):
    imageio.mimsave(
        "timg.gif",
        [imageio.imread(filename) for filename in sorted(glob(filepattern), key=lambda x: os.path.getmtime(x))],
        "GIF",
        duration = 1
    )

def main():
    for i in range(1, 50):
        show_picture(m=i)
    show_gif()   
    
    
        
if __name__ == "__main__":
    main()
