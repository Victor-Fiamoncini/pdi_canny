
import cv2
from matplotlib import pyplot as plt

from infra.filter_appliers.contracts.filter_applier import FilterApplier

class OpencvFilterApplier(FilterApplier):
  def apply_filter(self, img: str):
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(121),plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
