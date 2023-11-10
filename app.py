from flask import Flask, render_template, request, send_file
from generate import convertPDF

from PIL import Image

import os
from PIL import Image
import uuid
app = Flask(__name__)
# folder_path = f"{os.getcwd()}/tempFilesPDF/"
# files = os.listdir(folder_path)
# for file in files:
#     file_path = os.path.join(folder_path, file)
#     os.remove(file_path)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods = ['GET', 'POST'])
def convert():
    up_files = request.files.getlist('up-files')
    print(up_files) #For debugging

    unique_key = str(uuid.uuid4())[:6]#creates a unique Id for every Image
    cd = os.getcwd()
    relative =str("tempFilesPDF/"+ unique_key+".pdf")
    
    outFile =  os.path.join(cd, relative )
    try:
        
        convertPDF(up_files, outFile)
        
        print("converted")
        downL(outFile=outFile)
        print("downloaded")
        return send_file(outFile, as_attachment=True)

        # return render_template("Success.html")
    except Exception as e:
        print(e)
        return render_template("error.html")
  




def is_jpeg(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == 'JPEG'
    except Exception as e:
        # Handle exceptions (file not found, not an image, etc.)
        print(f"Error: {e}")
        return False


@app.route("/downL", methods = ['POST'])
def downL(outFile):
    return send_file(outFile, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)