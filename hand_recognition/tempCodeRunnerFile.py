        for id in range(0, 5):

            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:

                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)