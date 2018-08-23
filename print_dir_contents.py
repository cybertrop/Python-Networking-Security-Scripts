def print_dir_contents(sPath):
  import os
  for sChild in os.listdir(sPath):
  sChildPath = os.path.join(sPath, sChild)
  if os.apth.isdir(sChildPath):
      print_dir_contents(sChildPath)
  else:
      print(sChildPath)
   
print_dir_contents(<insert PWD here>)
