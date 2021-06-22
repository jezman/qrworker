import argparse
from pdfprocessing import split_pdf

ROWS = [4, 6, 8]
COLUMNS = [1, 2, 3]

parser = argparse.ArgumentParser()
parser.add_argument('files', type=argparse.FileType('r'), nargs='+')
parser.add_argument("-r", "--row", type=int, choices=ROWS, help="rows count", required=True)
parser.add_argument("-c", "--column", type=int, choices=COLUMNS, help="column count", required=True)
parser.add_argument("-v", "--verbose", type=bool, default=False, required=False)

args = parser.parse_args()

if __name__ == "__main__":
    for file in args.files:
        split_pdf(file.name, args.row, args.column, args.verbose)
