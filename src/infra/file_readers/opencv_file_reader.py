import os
import cv2

from infra.file_readers.contracts.file_reader import FileReader

class OpencvFileReader(FileReader):
  def read_file(file_path: str):
    cwd = os.getcwd()
    file_full_path = os.path.join(cwd, file_path)

    return cv2.imread(file_full_path, 0)
