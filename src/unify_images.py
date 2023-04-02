import cv2
import os


if __name__ == "__main__":
    path = "../flags"
    flags = os.listdir(path)
    X = 720
    Y = 720
    for flag in flags:
        flag_path = path + "/" + flag
        img = cv2.imread(flag_path)
        img = cv2.resize(img, (X, Y))
        cv2.imwrite(flag_path, img)








