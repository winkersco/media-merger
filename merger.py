import argparse
import os
import sys
import ffmpy

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-filenames', dest='input_filenames', nargs='+', help='input filenames seperated by space')
parser.add_argument('-o', '--output-filename', dest='output_filename', required=True, help='output filename')
args = parser.parse_args()

for input_filename in args.input_filenames:
    if not os.path.exists(input_filename):
        print(f'[-] Input file [{input_filename}] not found.')
        sys.exit()

if os.path.exists(args.output_filename):
    print(f'[-] Output file exist.')
    sys.exit()

inputs = {}
for input_filename in args.input_filenames:
    inputs[input_filename] = None
outputs = {args.output_filename: '-c:v copy'}

ff = ffmpy.FFmpeg(inputs=inputs, outputs=outputs)
ff.run()
