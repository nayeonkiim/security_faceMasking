import cv2
import numpy as np
from PIL import Image

imageFile='C:/opencv/4m20/human1.jpg'
img = cv2.imread(imageFile, 0)
height, width = img.shape

# 사진 4분의 1 numpy 정의
a = np.arange(width//2 * height//2).reshape(height//2, width//2)

# 1사분면
for j in range( 0, height//2):
    for i in range(0, width//2):
        a[j,i] = img[j,i]

# numpy를 이미지 포맷으로 만들기
pil_image=Image.fromarray(a)

# RGB mode가 아니라면 RGB mode로 변경
if pil_image.mode != 'RGB':
    pil_image = pil_image.convert('RGB')

# 4분의 1 영역 저장
pil_image.save('C:/opencv/4m20/human2.jpg', 'JPEG')

#cv2.imshow('sample',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



















