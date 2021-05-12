import cv2
r_values = []
g_values = []
b_values = []

ranges = [(0, 0, 0), (0, 0, 0)]

cap = cv2.VideoCapture(0)

frame = None


def mouse_handler(event, x, y, flags, params):
    global r_values, g_values, b_values
    if event == cv2.EVENT_LBUTTONDOWN:
        print("L mouse down")
        r_values.append(frame[y, x][2])
        g_values.append(frame[y, x][1])
        b_values.append(frame[y, x][0])
    if event == cv2.EVENT_RBUTTONDOWN:
        print("r mouse down")
        r_values.pop()
        g_values.pop()
        b_values.pop()


cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_handler)

while True:
    _, frame = cap.read()
    if(len(r_values)):
        ranges[0] = (int(min(b_values)),
                     int(min(g_values)), int(min(r_values)))
        ranges[1] = (int(max(b_values)), int(
            max(g_values)), int(max(r_values)))
    print(ranges)
    mask = cv2.inRange(frame, ranges[0], ranges[1])
    mask = cv2.medianBlur(mask, 13)
    cv2.imshow("mask", mask)
    cnts, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if w*h > 400:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
