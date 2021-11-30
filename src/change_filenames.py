import os
from shutil import copyfile

dir1 = "live"
dir2 = "live"
out_dir = "live2"

for folder in os.listdir(dir1):
    # iterative over each letter folder

    # make a new directory in the new location with the letter name
    os.makedirs(os.path.join(out_dir, folder), exist_ok=True)

    file_count = 0 # to index our file
    if folder == 'a':
        for f in os.listdir(os.path.join(dir1, folder)):
            # for each file f in the first folder 
            # copy this file to the new directory loc and add 1 to file_count
            copyfile(os.path.join(dir1, folder, f), os.path.join(out_dir, folder, f))
            file_count += 1 

        for f in os.listdir(os.path.join(dir2, folder)):
            # for each file in the second directory 
            # rename appropriately 
            os.rename(os.path.join(dir2, folder, f), os.path.join(dir2, folder, str(file_count) + ".png"))
            # now make a copy of this new named filename in the out_dir
            copyfile(os.path.join(dir2, folder, str(file_count) + ".png"), os.path.join(out_dir, folder, f))
            file_count += 1
