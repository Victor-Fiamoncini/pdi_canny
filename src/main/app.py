import os
import cv2 as cv
from matplotlib import pyplot as plt


if __name__ == "__main__":
  cwd = os.getcwd()
  input_file_full_path = os.path.join(cwd, 'files/input/file01.jpg')

  print(input_file_full_path)

  try:
    img = cv.imread(input_file_full_path, 0)
    edges = cv.Canny(img, 100, 200)

    plt.subplot(121),plt.imshow(img,cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
  except Exception as ex:
    print(ex)
