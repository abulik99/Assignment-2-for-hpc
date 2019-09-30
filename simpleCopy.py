from time import time
import shutil
import glob
import os

def main():
    if os.path.exists("./NewDirectory"):
        shutil.rmtree("./NewDirectory")
    os.mkdir("./NewDirectory")

    for name in glob.glob("./OldDirectory/*"):
        shutil.copy(name,"./NewDirectory")

if __name__ == "__main__":
    start_time = time()
    main()
    print("--- %s seconds ---" % (time() - start_time))