from reportlab.pdfgen import canvas
from PIL import Image
# yayyy this works! 
# big thanks to chat GPT!
def convertPDF(input_files, output_file):
    pdf = canvas.Canvas(output_file)

    # Set the page size based on the first image
    first_img = Image.open(input_files[0])
    width, height = first_img.size
    pdf.setPageSize((width, height))

    for input_file in input_files:
        img = Image.open(input_file)
        pdf.drawInlineImage(img, 0, 0, width, height)
        pdf.showPage()  # Start a new page for each image

    pdf.save()


# input_files = ['soh.jpg', 'args.jpg']
# output_file = 'output.pdf'

# convert_jpgs_to_pdf(input_files, output_file)
