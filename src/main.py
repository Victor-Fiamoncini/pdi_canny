from factories.apply_canny_filter_service_factory import ApplyCannyFilterServiceFactory

if __name__ == "__main__":
  file_path = 'files/input/file01.jpg'

  try:
    ApplyCannyFilterServiceFactory.make().exec(file_path)
  except Exception as ex:
    print(f'Error raised: {ex}')
