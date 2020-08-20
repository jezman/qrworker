# QRWorker

Обработка PDF файлов присланных "Честным знаком"

## Установка

```sh
git clone "https://github.com/jezman/qrworker"
cd qrworker
pip install -r requirements.txt

```

## Возможности

- Разделяет PDF файлы формата А4 с 4,6 или 8 этикетками на странице. Создает новый файл, формата этикетки, с 1 этикеткой на странице, для возможности печати на принтере
- Считывает коды из PDF, сохраняет в отдельный файл

## Пример
```sh
usage: qrworker.py [-h] [-n {4,6,8}] [-c] files [files ...]

positional arguments:
  files

optional arguments:
  -h, --help            show this help message and exit
  -n {4,6,8}, --number {4,6,8}
                        number QR codes per page
  -c, --codes           save codes in file
```

```sh
python3 qrworker.py to_split1.pdf to_split2.pdf to_split3.pdf -n 6 -c

Splitted complete: Splitted_to_split1.pdf
Parse complete, codes saved: to_split1.txt
Splitted complete: Splitted_to_split2.pdf
Parse complete, codes saved: to_split2.txt
Splitted complete: Splitted_to_split3.pdf
Parse complete, codes saved: to_split3.txt
```

## License

MIT © 2020 jezman
