from time import time
import shutil
import os
import glob
import multiprocessing 

def copyFile(filePath, destDirectory):
    shutil.copy(filePath, destDirectory)


def main():
    if os.path.exists("./NewDirectory"):
        shutil.rmtree("./NewDirectory")
    os.mkdir("./NewDirectory")

    processList = []
    for name in glob.glob("./OldDirectory/*"):
        processList.append(multiprocessing.Process(target=copyFile, args=(name,"./NewDirectory")))
        processList[len(processList)-1].start()

    for process in processList:
        process.join()


if __name__ == "__main__":
    start_time = time()
    main()
    print("Multiprocessing --- %s seconds ---" % (time() - start_time))