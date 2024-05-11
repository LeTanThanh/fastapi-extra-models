import sys

paths = __file__.split("/")
paths.pop()
paths.pop()

ROOT_DIR = ("/").join(paths)

sys.path.append(ROOT_DIR)
