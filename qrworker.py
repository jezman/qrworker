import argparse
from pdfprocessing import split_pdf

ALLOWED_NUMBERS = [4, 6, 8]

parser = argparse.ArgumentParser()
parser.add_argument('files', type=argparse.FileType('r'), nargs='+')
parser.add_argument("-n", "--number", type=int, choices=ALLOWED_NUMBERS,
                    help="number QR codes per page")

args = parser.parse_args()


if __name__ == "__main__":
    for file in args.files:
        split_pdf(file.name, args.number)
