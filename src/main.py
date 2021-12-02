from infra.file_readers.opencv_file_reader import OpencvFileReader
from infra.filter_appliers.opencv_filter_applier import OpencvFilterApplier
from services.apply_canny_filter_service import ApplyCannyFilterService

if __name__ == "__main__":
  file_path = 'files/input/file01.jpg'

  try:
    file_reader =  OpencvFileReader()
    filter_applier =  OpencvFilterApplier()
    apply_canny_filter_service = ApplyCannyFilterService(file_reader, filter_applier)

    apply_canny_filter_service.exec(file_path)
  except Exception as ex:
    print(ex)
