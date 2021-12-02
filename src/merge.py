import os
import sys
from glob import glob
from shutil import copyfile
import string
import threading


def move_class(dir1, dir2, dir_out, class_name):
    dir1_pics = sorted(glob(os.path.join(dir1, class_name, "*.jpg")))
    dir2_pics = sorted(glob(os.path.join(dir2, class_name, "*.jpg")))
    print(f"merging {len(dir1_pics)} + {len(dir2_pics)} for {class_name}")
    all_pics = dir1_pics + dir2_pics
    if len(all_pics) == 0:
        return
    os.makedirs(os.path.join(dir_out, class_name), exist_ok=True)
    for i, pic in enumerate(all_pics):
        output_file = os.path.join(dir_out, class_name, f"{i}.jpg")
        copyfile(pic, output_file)


def main(dir1, dir2, dir_out):
    classes = list(string.ascii_lowercase) + ["z_blank"]
    threads = []
    for c in classes:
        thread = threading.Thread(
            target=move_class,
            args=(dir1, dir2, dir_out, c)
        )
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

