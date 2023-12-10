import cv2
import numpy as np

# 상의 색상 판별 함수
def detect_clothing_color(image, box):
    x, y, w, h = box
    roi = image[y:y + h, x:x + w]

    # 여기에서 색상을 판별하는 로직을 추가해야 합니다.
    # 예를 들면, 평균 색상을 계산하거나 다른 색상 특징을 이용할 수 있습니다.

    # 임시로 랜덤 색상을 반환하는 코드
    return tuple(np.random.randint(0, 255, 3).tolist())

# HOG 디텍터 생성
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 동영상 열기
cap = cv2.VideoCapture('v2.mp4')

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        break

    # 보행자 검출
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(4, 4), scale=1.05)

    # 검출된 보행자 표시
    for i, (x, y, w, h) in enumerate(boxes):
        # 상의 색상 판별
        clothing_color = detect_clothing_color(frame, (x, y, w, h))

        # 박스 색상 지정
        cv2.rectangle(frame, (x, y), (x + w, y + h), clothing_color, 2)

    # 획득된 보행자 수 표시
    cv2.putText(frame, f'Pedestrians: {len(boxes)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 화면에 출력
    cv2.imshow('Pedestrian Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()