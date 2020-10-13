import os
import re
counter =0

directory_location = "Enter your Directory Path Here"

for root, subdirs, files in os.walk(dir_loc):
    for name in files:
        file_name = name..split(".")
        legalname = re.sub('[^A-Za-z0-9]+ ', ' ', file_name[0]) + file_name[1]
        if legalname != file_name[0]:
            counter = counter+1
            os.rename(os.path.join(root,name), os.path.join(root,legalname))
print(counter)
