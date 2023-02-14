#import pytesseract
from wand.image import Image
import os

os.chdir("/Users/zalazhar/projects/RR/")
filename = "pdfs/apr_1904.pdf"


# Open the PDF file
filenames = [filename]
with Image(filename= filename, resolution=600) as img:
    # Iterate over each page in the PDF file
    for i, page in enumerate(img.sequence):
        # Convert the page to a PNG image
        with Image(page) as png:
            png.format = 'png'
            png_filename = f'mozilla_page{i}.png'
            png.save(filename=png_filename)
            filenames.append(png_filename)
            print(i)

 
for filename in filenames:
        # Apply OCR to the image and extract text
        print(filename)
        filename_to = filename.replace(".png","" )
        cmd = f'tesseract -l eng+ara  {filename} {filename_to}'
        os.system(cmd)

              
       
        
        