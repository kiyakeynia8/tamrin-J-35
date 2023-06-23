import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
rows ,cols, chanel = frame.shape
writer = cv2.VideoWriter("output/2_output.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    ret, frame = cap.read()
    
    frame[220:260,300:305] = 0
    frame[220:225,300:340] = 0
    frame[260:265,300:340] = 0
    frame[220:265,340:345] = 0

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    check_r = frame[225:260,305:340, 0]
    print(np.average(check_r),"r")
    check_g = frame[225:260,305:340, 1]
    print(np.average(check_g),"g")
    check_b = frame[225:260,305:340, 2]
    print(np.average(check_b),"b")

    if 0 <= np.average(check_r) <= 100 and 0 <= np.average(check_g) <= 100 and 0 <= np.average(check_b) <= 100:
        cv2.putText(frame,"Black",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 130 <= np.average(check_r) <= 255 and 130 <= np.average(check_g) <= 255 and 130 <= np.average(check_b) <= 255:
        cv2.putText(frame,"White",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 140 <= np.average(check_r) <= 255 and 45 <= np.average(check_g) <= 90 and 100 <= np.average(check_b) <= 150:
        cv2.putText(frame,"Red",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 60 <= np.average(check_r) <= 90 and 100 <= np.average(check_g) <= 255 and 130 <= np.average(check_b) <= 185:
        cv2.putText(frame,"Green",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    elif 70 <= np.average(check_r) <= 110 and 70 <= np.average(check_g) <= 110 and 150 <= np.average(check_b) <= 255:
        cv2.putText(frame,"Blue",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    elif 150 <= np.average(check_r) <= 255 and 150 <= np.average(check_g) <= 255 and 80 <= np.average(check_b) <= 130:
        cv2.putText(frame,"Yellow ",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    elif 190 <= np.average(check_r) <= 240 and 70 <= np.average(check_g) <= 100 and 50 <= np.average(check_b) <= 100:
        cv2.putText(frame,"Orange",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    if not ret:
        break

    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()