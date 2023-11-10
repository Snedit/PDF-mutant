"""from reportlab.pdfgen import canvas
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


input_files = ['soh.jpg', 'args.jpg']
output_file = 'output.pdf'

convertPDF(input_files, output_file)"""
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO
from reportlab.lib.pagesizes import portrait

def convertPDF(input_files, output_file):
    pdf = canvas.Canvas(output_file)

    for input_file in input_files:
        # Open the image using PIL
        img = Image.open(input_file)

        # Set the page size based on the image size
        page_width, page_height = portrait(img.size)
        pdf.setPageSize((page_width, page_height))

        # Calculate the position to center the image on the page
        x_offset = (page_width - img.width) / 2
        y_offset = (page_height - img.height) / 2

        # Save the image to a BytesIO buffer with adjusted quality
        img_buffer = BytesIO()
        img.save(img_buffer, format='JPEG', quality=100)
        img_buffer.seek(0)

        # Create a new Image object from the BytesIO buffer
        img = Image.open(img_buffer)

        pdf.drawInlineImage(img, x_offset, y_offset, width=img.width, height=img.height)
        pdf.showPage()  # Start a new page for each image

    pdf.save()

# Example usage
# input_files = ['soh.jpg', 'args.jpg', 'city.png', 'kitten.png']
# output_file = 'output.pdf'

# convertPDF(input_files, output_file)


