from copy import copy
from PyPDF2 import PdfFileWriter, PdfFileReader


def get_coordinations(rows):
    if rows == 4:
        return {'x_left': 21, 'x_right': 119, 'y_top': 822, 'y_bottom': 652, 'qr_heigh': 186, 'qr_width': 0}
    elif rows == 6:
        return {'x_left': 21, 'x_right': 190, 'y_top': 822, 'y_bottom': 723, 'qr_hight': 118, 'qr_width': 0}
    elif rows == 8:
        return {'x_left': 0, 'x_right': 169, 'y_top': 844, 'y_bottom': 750, 'qr_hight': 102, 'qr_width': 172}

def split_pdf(filename, rows, columns):
    with open(filename, 'rb') as in_f:
        pdf_input = PdfFileReader(in_f)
        pdfWriter = PdfFileWriter()

        num_pages = PdfFileReader(in_f).numPages

        for num_page in range(num_pages):
            for column in range(columns):
                coordinates = get_coordinations(rows)

                for count in range(rows):
                    pdf = copy(pdf_input.getPage(num_page))

                    pdf.cropBox.lowerLeft = (coordinates['x_left'], coordinates['y_top'])
                    pdf.cropBox.upperRight = (coordinates['x_right'], coordinates['y_bottom'])

                    coordinates['y_top'] -= coordinates['qr_hight']
                    coordinates['y_bottom'] -= coordinates['qr_hight']
                    
                    # Blank page check
                    if len(pdf['/Resources']['/XObject']) > 10:
                            pdfWriter.addPage(pdf)

                if columns > 1:
                    coordinates['x_left'] += coordinates['qr_width']
                    coordinates['x_right'] += coordinates['qr_width'] 


        with open('Splitted_{}'.format(filename), 'wb') as out_f:
            pdfWriter.write(out_f)
            print('Splitted complete: {}'.format(filename))
