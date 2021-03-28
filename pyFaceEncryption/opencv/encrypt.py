import hashlib

import imageio
import numpy as np
import matplotlib.pyplot as plt


def kaleidoscope(image, message, noise=0):
    m = hashlib.sha512()
    m.update(message.encode())
    hashed = m.digest()

    masked = image.copy()
    masked_list = masked.reshape((1, masked.size)).tolist()

    noise_list = np.random.normal(0, noise, masked.size).tolist()
    for i in range(len(masked_list[0])):
        value = max(0, min(255, masked_list[0][i] + int(noise_list[i])))
        masked_list[0][i] = value ^ hashed[i % 64]

    masked = np.array(masked_list, dtype=np.uint8).reshape(masked.shape)
    return masked


# 코드 : https://minhwan.kim/kaleidoscope-symmetric-image-encryption-decryption/