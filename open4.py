import cv2
import numpy as np

# YOLO 모델 설정
net = cv2.dnn.readNet('yolov3.cfg', 'yolov3.weights')
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getUnconnectedOutLayersNames()

# 이미지 읽기
img = cv2.imread('um.jpg')
height, width, _ = img.shape

# YOLO 입력 형식으로 이미지 전처리
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(layer_names)

# 검출된 객체 필터링
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5 and class_id == 2:  # 클래스 ID 2는 'person'
            center_x, center_y, w, h = (detection[:4] * np.array([width, height, width, height])).astype(int)
            x, y = int(center_x - w / 2), int(center_y - h / 2)
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

# 비최대 억제(NMS)를 적용하여 중복 검출 제거
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# 우산을 쓴 사람에 대한 검출 결과 표시
for i in indices:
    i = i[0]
    box = boxes[i]
    x, y, w, h = box
    label = f'Person with Umbrella: {confidences[i]:.2f}'
    color = (0, 255, 0)  # 초록색으로 표시
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# 결과를 화면에 표시
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()