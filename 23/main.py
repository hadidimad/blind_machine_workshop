import cv2
h_values = []
s_values = []
v_values = []

ranges = [(0, 0, 0), (0, 0, 0)]

cap = cv2.VideoCapture(0)

frame = None


def mouse_handler(event, x, y, flags, params):
    global h_values, s_values, v_values, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        print("L mouse down")
        h_values.append(frame[y, x][0])
        s_values.append(frame[y, x][1])
        v_values.append(frame[y, x][2])
    if event == cv2.EVENT_RBUTTONDOWN:
        print("r mouse down")
        h_values.pop()
        s_values.pop()
        v_values.pop()


cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_handler)

while True:
    _, frame = cap.read()
    img_rbg = frame.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if(len(h_values)):
        ranges[0] = (int(min(v_values)*0.9),
                     int(min(s_values)*0.9), int(min(h_values)*0.9))
        ranges[1] = (int(max(v_values)), int(
            max(s_values)), int(max(h_values)))
    print(ranges)
    mask = cv2.inRange(frame, ranges[0], ranges[1])
    mask = cv2.medianBlur(mask, 13)
    cv2.imshow("mask", mask)
    cnts, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if w*h > 400:
            cv2.rectangle(img_rbg, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("rgb", img_rbg)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
