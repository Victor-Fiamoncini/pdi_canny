from infra.file_readers.opencv_file_reader import OpencvFileReader
from infra.filter_appliers.opencv_filter_applier import OpencvFilterApplier
from services.apply_canny_filter_service import ApplyCannyFilterService

class ApplyCannyFilterServiceFactory:
  @staticmethod
  def make():
    file_reader = OpencvFileReader()
    filter_applier = OpencvFilterApplier()

    return ApplyCannyFilterService(file_reader, filter_applier)
