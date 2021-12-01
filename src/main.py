import os

if __name__ == "__main__":
  cwd = os.getcwd()
  full_path = os.path.join(cwd, '')

  try:
    print(full_path)
  except Exception as ex:
    print(ex)
