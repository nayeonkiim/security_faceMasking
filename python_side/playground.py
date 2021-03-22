# import cv2
# cap = cv2.VideoCapture(1) # 노트북 웹캠을 카메라로 사용: 0
# cap.set(3,1920) # 너비
# cap.set(4,1080) # 높이
#
# while (True):
#     ret, frame = cap.read()
#     cv2.imshow('result', frame)
#
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:  # Esc 키를 누르면 종료
#         break
#
# cap.release()
# cv2.destroyAllWindows()

s = [b'\xff' * 46080 for x in range(20)]
print(s[0])