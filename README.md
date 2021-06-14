# CCTV에서 딥페이크를 방지하는 방법
- 얼굴이 촬영 된 사진, 영상을 가지고 딥페이크에 악용되는 것을 방지하기 위해 촬영되는 영상에서 얼굴부분을 인식하여 모자이크 처리를 하고 영상을 저장한다. 
- 복호화가 필요한 경우를 대비하여 모자이크가 되기 전에 이미지를 1초에 한번씩 캡쳐, Base64URL로 변환 후 url을 aes 암호화를 수행하여 binary 파일로 저장한다. 
- 암호화 된 파일을 추후에 필요한 경우 aes 복호화하여 이미지를 확인한다. 
- 웹을 통해 날짜와 시간을 입력하면 복호화된 이미지, 영상 확인 가능하다.

## 사용 기술
- OpenCV 및 python
- node.js & express
- Mysql

## database
<img src="https://user-images.githubusercontent.com/61819669/121828157-b88b6c00-ccf9-11eb-9b48-19dea2735f11.png">


