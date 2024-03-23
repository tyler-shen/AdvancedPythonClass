# import os
# os.remove("test.txt")

# file = open("test.txt", "w")
# file.write("new line")
# file.close()

import os
file_name = "test.txt"
if os.path.exists(file_name):
  os.remove(file_name)
else:
  # raise Exception("file doesn't exist!")
  print(f"file {file_name} doesn't exist!")

# file_name = "test.txt"
# try:
#     os.remove(file_name)
# except FileNotFoundError:
#     print("file not existed")
# except:
#     print("something goes wrong")
