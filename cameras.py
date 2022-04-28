import cv2
import numpy as np
import triangulation as tri



def stereoVision():
    B = 7
    f = 4
    frame_rate = 30
    alpha = 53.4
    count = 15

    capL = cv2.VideoCapture(0)
    capR = cv2.VideoCapture(2)

    capL.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    capR.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

    while capL.isOpened() and capR.isOpened():
        retL, imgL = capL.read()
        retR, imgR = capR.read()
        
        gimgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
        gimgR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("Left", imgL)
        cv2.imshow("Right", imgR)
        cv2.waitKey(5)
        if not retL or not retR:
            break
        if count > 10:
            sucL, cornersL = cv2.findChessboardCorners(gimgL, (5, 3), None)
            sucR, cornersR = cv2.findChessboardCorners(gimgR, (5, 3), None)
            count = 0

        if sucL:
            cornersL = np.squeeze(cornersL)
            bboxL = (int(cornersL[0][0]), int(cornersL[0][1]), int(cornersL[14][0]), int(cornersL[14][1]))

            centerLB = ((bboxL[0] + bboxL[2]) / 2, (bboxL[1] + bboxL[3]) / 2)

            bboxL = (int(centerLB[0] - 25), int(centerLB[1] - 25), int(centerLB[0] + 25), int(centerLB[1] + 25))

            cv2.rectangle(imgL, (bboxL[0], bboxL[1]), (bboxL[2], bboxL[3]), (255, 0, 0), 2, 1)

            cv2.imshow("Processed Left", imgL)
            cv2.waitKey(5)

        if sucR:
            cornersR = np.squeeze(cornersR)
            bboxR = (int(cornersR[0][0]), int(cornersR[0][1]), int(cornersR[14][0]), int(cornersR[14][1]))

            centerRB = ((bboxR[0] + bboxR[2]) / 2, (bboxR[1] + bboxR[3]) / 2)

            bboxR = (int(centerRB[0] - 25), int(centerRB[1] - 25), int(centerRB[0] + 25), int(centerRB[1] + 25))

            #print("right", bboxR)
            cv2.rectangle(imgR, (bboxR[0], bboxR[1]), (bboxR[2], bboxR[3]), (255, 0, 0), 2, 1)

            cv2.imshow("Processed Right", imgR)
            cv2.waitKey(5)

        if sucR and sucL:
            depth = tri.find_depth((bboxR[0] + bboxR[2] / 2, bboxR[1] + bboxR[3] / 2),
                               (bboxL[0] + bboxL[2] / 2, bboxL[1] + bboxL[3] / 2), imgR, imgL, B, f, alpha)
            print(depth)
        
        count = count+1
