from typing import Any
from errors.unimplemented_method_error import UnimplementedMethodError

class FilterApplier:
  def apply_filter(self, img: Any):
    raise UnimplementedMethodError()
