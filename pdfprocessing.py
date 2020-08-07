from copy import copy
from PyPDF2 import PdfFileWriter, PdfFileReader


def get_coordinations(qr_per_page):
    if qr_per_page == 4:
        return {'x_left': 21, 'x_right': 119,
                'y_top': 822, 'y_bottom': 652, 'qr_range': 186}
    elif qr_per_page == 6:
        return {'x_left': 21, 'x_right': 190,
                'y_top': 822, 'y_bottom': 723, 'qr_range': 118}
    elif qr_per_page == 8:
        pass


def split_pdf(filename, qr_per_page):
    with open(filename, 'rb') as in_f:
        pdf_input = PdfFileReader(in_f)
        pdfWriter = PdfFileWriter()

        num_pages = PdfFileReader(in_f).numPages

        for num_page in range(num_pages):
            coordinates = get_coordinations(qr_per_page)
            count = 0

            while count < qr_per_page:
                pdf = copy(pdf_input.getPage(num_page))

                pdf.cropBox.lowerLeft = (coordinates['x_left'], coordinates['y_top'])
                pdf.cropBox.upperRight = (coordinates['x_right'], coordinates['y_bottom'])

                coordinates['y_top'] -= coordinates['qr_range']
                coordinates['y_bottom'] -= coordinates['qr_range']

                count += 1

                pdfWriter.addPage(pdf)

        with open('Splitted_{}'.format(filename), 'wb') as out_f:
            pdfWriter.write(out_f)
            print('Complete {}'.format(filename))
