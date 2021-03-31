from copy import copy
from PyPDF2 import PdfFileWriter, PdfFileReader


def get_coordinations(qr_per_page):
    if qr_per_page == 4:
        return {'x_left': 21, 'x_right': 119, 'y_top': 822, 'y_bottom': 652, 'qr_range': 186}
    elif qr_per_page == 6:
        return {'x_left': 21, 'x_right': 190, 'y_top': 822, 'y_bottom': 723, 'qr_range': 118}
    elif qr_per_page == 8:
        return {'x_left': 0, 'x_right': 169, 'y_top': 844, 'y_bottom': 750, 'qr_range': 102}


def split_pdf(filename, qr_per_page):
    with open(filename, 'rb') as in_f:
        pdf_input = PdfFileReader(in_f)
        pdfWriter = PdfFileWriter()

        num_pages = PdfFileReader(in_f).numPages

        for num_page in range(num_pages):
            count = 0

            while count < qr_per_page:
                coordinates = get_coordinations(qr_per_page)
                COLUMNS = 3
                column = 0
                while column < COLUMNS:
                    pdf = copy(pdf_input.getPage(num_page))

                    pdf.cropBox.lowerLeft = (coordinates['x_left'], coordinates['y_top'])
                    pdf.cropBox.upperRight = (coordinates['x_right'], coordinates['y_bottom'])

                    coordinates['x_left'] = coordinates['x_left'] + 172
                    coordinates['x_right'] = coordinates['x_right'] + 172 

                    column += 1

                    pdfWriter.addPage(pdf)

                count += 1
                coordinates['y_top'] -= coordinates['qr_range']
                coordinates['y_bottom'] -= coordinates['qr_range']

        with open('Splitted_{}'.format(filename), 'wb') as out_f:
            pdfWriter.write(out_f)
            print('Splitted complete: {}'.format(filename))
