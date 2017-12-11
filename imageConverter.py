from PIL import Image
import glob, os
import config as cfg

def imageConverter():
    size = cfg.imageConverter['imageHeight'], cfg.imageConverter['imageWidth']
    src =  cfg.imagePath['dest']
   
    print("Converting Image..")
    for infile in glob.glob( cfg.imageConverter['fileExtension']):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + 'new' + ".jpg", "JPEG") #thumbnail