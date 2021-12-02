from infra.file_readers.contracts.file_reader import FileReader

class ApplyCannyFilterService:
  def __init__(self, file_reader: FileReader, canny_filter_applier):
    self.file_reader = file_reader
    self.canny_filter_applier = canny_filter_applier
