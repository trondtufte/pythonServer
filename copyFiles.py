import os
import shutil
import glob
import os
import config as cfg

def copyFiles():
    src = cfg.imagePath['src']    #"D:\\DATA\\Ek80 Images"
    dest = cfg.imagePath['dest']  #"C:\\appl\EchoImage\\images"

    for root, dirs, files in os.walk(src): 
        for file in files:
            path_file = os.path.join(root,file)
        #shutil.copy2(path_file,dest)
        #shutil.move(path_file,dest)

    # Getting the latest file
    list_of_files = glob.glob(src + cfg.imagePath['fileExtension'] ) # *.jpg '/*'
    latest_file = min(list_of_files, key=os.path.getctime)
    print("Copying latest file: " + latest_file)
    shutil.copy2(latest_file,dest)

