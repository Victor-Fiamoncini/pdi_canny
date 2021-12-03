from errors.apply_canny_filter_error import ApplyCannyFilterError
from infra.file_readers.contracts.file_reader import FileReader
from infra.filter_appliers.contracts.filter_applier import FilterApplier

class ApplyCannyFilterService:
  def __init__(self, file_reader: FileReader, canny_filter_applier: FilterApplier):
    self._file_reader = file_reader
    self._canny_filter_applier = canny_filter_applier

  def exec(self, file_path: str):
    try:
      img = self._file_reader.read_file(file_path)
      self._canny_filter_applier.apply_filter(img, 300, 400)
    except:
      raise ApplyCannyFilterError()
