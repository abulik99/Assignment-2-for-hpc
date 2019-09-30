from time import time
import shutil
import os
import glob
import threading

def copyFile(filePath, destDirectory):
    shutil.copy(filePath, destDirectory)


def main():
    if os.path.exists("./NewDirectory"):
        shutil.rmtree("./NewDirectory")
    os.mkdir("./NewDirectory")

    threadList = []
    for name in glob.glob("./OldDirectory/*"):
        threadList.append(threading.Thread(target=copyFile, args=(name,"./NewDirectory")))
        threadList[len(threadList) - 1].start()

    for thread in threadList:
        thread.join()


if __name__ == "__main__":
    start_time = time()
    main()
    print("Multithreading --- %s seconds ---" % (time() - start_time))