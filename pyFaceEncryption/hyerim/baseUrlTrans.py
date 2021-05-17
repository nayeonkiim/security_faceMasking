import numpy as np
import cv2
import time
import base64

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    time.sleep(10)
    ret, frame = cap.read()
    result, frame = cv2.imencode('.bmp', frame, [cv2.IMWRITE_WEBP_QUALITY, 100])
    print('----------encode-----------')
    print(result)
    print('encode Image : ', frame)
    b64data = base64.b64encode(frame)
    print('encode -> base64 : ', b64data)
    #위까지 base64로 인코딩  아래부터는 디코딩
    print('---------decode---------')
    frame = base64.b64decode(b64data)
    print('decodebase64 : ', frame)
    froms = np.frombuffer(frame, dtype='uint8')
    print('?? : ', froms)
    frame = cv2.imdecode(froms,cv2.IMREAD_COLOR)
    cv2.imshow("test", frame)
    if cv2.waitKey(1) > 0: break
cv2.destroyAllWindows()