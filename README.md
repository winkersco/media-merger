# Media Merger

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install -r requirements.txt
```

## Usage

```bash
usage: merger.py [-h] [-i INPUT_FILENAMES [INPUT_FILENAMES ...]] -o OUTPUT_FILENAME

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILENAMES [INPUT_FILENAMES ...], --input-filenames INPUT_FILENAMES [INPUT_FILENAMES ...]
                        input filenames seperated by space
  -o OUTPUT_FILENAME, --output-filename OUTPUT_FILENAME
                        output filename
```

## Example

Below commad merge `file1.webm` and `file2.webm` into single file `output.mp4`.

```bash
python merger.py -i file1.webm file2.webm  -o output.mp4
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)