## Basic code to convert the pdf to python

from pdf2image import convert_from_path
from PIL import Image
import os

pdf_path = "../Forms"

## traverse all the files in forms folder to read all the pdfs

##

output_folder = "../Data/"
def convert_pdfs_to_images(folder_path, output_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                images = convert_from_path(file_path)
                file_name = os.path.splitext(file)[0]
                for i, image in enumerate(images):
                    image.save(f"{output_path}/{file_name}_{i}.jpg", "JPEG")


convert_pdfs_to_images(pdf_path, output_folder)




