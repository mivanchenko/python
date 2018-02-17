import os

for root, dirs, files, rootfd in os.fwalk(os.getcwd()):
   print(root, "consumes", end=" ")
   print(sum([os.stat(name, dir_fd=rootfd).st_size for name in files]),
         end=" ")
   print("bytes in", len(files), "non-directory files")
   if '.git' in dirs:
       dirs.remove('.git')  # don't visit git directories
