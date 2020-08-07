from copy import copy
from numpy import savetxt
from pdftotext import PDF as pdf_to_text
from PyPDF2 import PdfFileWriter, PdfFileReader

IGNORE_LIST = ['МОДЕЛЬ', 'РАЗМЕР', '--', '']


def get_coordinations(qr_per_page):
    if qr_per_page == 4:
        return {'x_left': 21, 'x_right': 119,
                'y_top': 822, 'y_bottom': 652, 'qr_range': 186}
    elif qr_per_page == 6:
        return {'x_left': 21, 'x_right': 190,
                'y_top': 822, 'y_bottom': 723, 'qr_range': 118}
    elif qr_per_page == 8:
        return {'x_left': 0, 'x_right': 169,
                'y_top': 844, 'y_bottom': 750, 'qr_range': 102}


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
            print('Splitted complete: {}'.format(filename))


def parse_pdf(pdf_file):
    codes = list()

    for page in pdf_file:
        page = page.split('\n')
        page = [code.strip() for code in page if code not in IGNORE_LIST]

        # joins codes from two lines
        two_codes = ([''.join(page[i:i + 2]) for i in range(0, len(page), 2)])
        [codes.append(code) for code in two_codes]

    return codes


def save_codes(pdf_file):
    with open(pdf_file, "rb") as fl:
        pdf = pdf_to_text(fl)
        codes = parse_pdf(pdf)
        codes = [code.replace('"', '""') for code in codes]

        name_to_save = pdf_file.split('.')[0] + ".txt"
        savetxt(name_to_save, codes, fmt='"%s"', delimiter=",")

        print('Parse complete, codes saved - {}'.format(name_to_save))
