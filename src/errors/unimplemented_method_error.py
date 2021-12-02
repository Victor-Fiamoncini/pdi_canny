class UnimplementedMethodError(Exception):
  def __init__(self):
    super().__init__('UnimplementedMethodError')
