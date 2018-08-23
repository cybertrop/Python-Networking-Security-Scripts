# This is a quick script that will let you print the contents of your present working directory


def print_dir_contents(sPath): # Create a function with sPath parameter
  """ Import the os mod
      iterate through listdir method of the source path
      conditional if the path is the dir then print the dir
      else print the child path
  """
  
  import os
  for sChild in os.listdir(sPath):
  sChildPath = os.path.join(sPath, sChild)
  if os.path.isdir(sChildPath):
      print_dir_contents(sChildPath)
  else:
      print(sChildPath)
   
print_dir_contents(<insert PWD here>)
