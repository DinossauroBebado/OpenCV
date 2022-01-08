font = cv2.FONT_HERSHEY_SIMPLEX
        name = labels[id_]
        color = (255, 255, 255)
        stroke = 2
        cv2.putText(frame, name, (x, y), font, 1,
                    color, stroke, cv2.LINE_AA)