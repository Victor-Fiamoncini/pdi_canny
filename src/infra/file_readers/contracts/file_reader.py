from typing import Any
from errors.unimplemented_method_error import UnimplementedMethodError

class FileReader:
  def read_file(self, file_path: str) -> Any:
    raise UnimplementedMethodError()
