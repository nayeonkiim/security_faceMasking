import encrypt;
import matplotlib.pyplot as plt
import imageio

# 복호화 방법 생각해보기
getPic = "C:/opencv/4m20/9.58.51.jpg";

face = imageio.imread(getPic)
decrypted = encrypt.kaleidoscope(face, 'pocari sweat', 50);
plt.imshow(decrypted)
plt.show()