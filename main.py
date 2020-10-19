import os
import re
counter =0
dir_loc = "Enter your Directory Location Here"

for root, subdirs, files in os.walk(dir_loc):
    for name in files:
        file_name = name.split(".")
        legal_name = re.sub('[^A-Za-z0-9]+ ', ' ', file_name[0]) +"."+ file_name[1]
        if legal_name != name:
            counter = counter+1
            os.rename(os.path.join(root,name), os.path.join(root,legal_name))
print(counter+' files renamed')
