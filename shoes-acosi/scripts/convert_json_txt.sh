#!/bin/bash

python3 scripts/convert_json_txt.py --input_file data/review_splits.json --output_file1 data/train.txt --output_file2 data/test.txt --output_file3 data/dev.txt

cp 