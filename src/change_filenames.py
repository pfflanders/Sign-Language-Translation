import os
import time

dir1 = "live"

for folder in os.listdir(dir1):
    for f in os.listdir(os.path.join(dir1, folder)):
        # for each file f in the first folder 
        os.rename(f, time.time_ns())