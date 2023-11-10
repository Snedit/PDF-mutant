from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

def convert_images_to_pdf(images, output_pdf_path):
    # Create a PDF file with A4 page size
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    for image in images:
        # Add a new page for each image

        # Resize the image to fit within the A4 page
        a4_width, a4_height = letter
        image.thumbnail((a4_width, a4_height))

        # Calculate the position to center the image on the page
        x_offset = (a4_width - image.width) / 2
        y_offset = (a4_height - image.height) / 2

        # Draw the image on the PDF page
        c.drawInlineImage(image, x_offset, y_offset, width=image.width, height=image.height)
        c.showPage()

    # Save the PDF file
    c.save()

# Example usage
image1 = Image.open('args.jpg')
image2 = Image.open('soh.jpg')

image_paths = [image1, image2]
output_pdf_path = 'output.pdf'

convert_images_to_pdf(image_paths, output_pdf_path)
