#import pytesseract
from wand.image import Image
import os
import time

os.chdir("/Users/zalazhar/projects/RR/")
filename = "pdfs/apr_1904.pdf"



filenames = ["pdfs/" + x for x in os.listdir("pdfs")]

for filename in [filenames[4]]: 
    
    print(filename)
    # # Open the PDF file
    png_files = []
    with Image(filename= filename, resolution=600) as img:
         # Iterate over each page in the PDF file
         for i, page in enumerate(img.sequence):
             # Convert the page to a PNG image
             with Image(page) as png:
                 png.format = 'png'
                 png_filename = f'mozilla_page{i}.png'
                 png.save(filename=png_filename)
                 png_files.append(png_filename)
           
                 print(i)


    directory =  filename.replace(".pdf","").replace("pdfs/","")

   
    if not os.path.exists(directory):
        os.mkdir( os.getcwd() + "/" + directory )
    print(os.getcwd() + "/" + directory)
    for png in png_files:
             # Apply OCR to the image and extract text
             png_to = png.replace(".png","" )
             print(png)
             cmd = f'tesseract -l eng+ara  {png} {png_to}'
             os.system(cmd)
    os.system(f"rm -rf *.png  ")
    os.system(f"mv *.txt {directory}")
                
        
        
        