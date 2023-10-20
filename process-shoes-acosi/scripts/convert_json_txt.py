import argparse
from json import load

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help="input json file", required=True)
parser.add_argument(
    "-1",
    "--output_file1",
    help="output json file",
    required=True,
)
parser.add_argument(
    "-2",
    "--output_file2",
    help="output json file",
    required=True,
)
parser.add_argument(
    "-3",
    "--output_file3",
    help="output json file",
    required=True,
)

args = parser.parse_args()

with open(args.input_file) as f:
    review_splits = load(f)

train = review_splits["train"]
test = review_splits["test"]
val = review_splits["validation"]

train_str_list = []
test_str_list = []
val_str_list = []

for rev in train:
    rev_str = (
        rev["review"]
        + "####"
        + str(rev["annot1"])
        .replace("#", " ")
        .replace("/", "_")
        .replace("\\\\_", "_")
        .lower()
    )
    train_str_list.append(rev_str)

for rev in test:
    rev_str = (
        rev["review"]
        + "####"
        + str(rev["annot1"])
        .replace("#", " ")
        .replace("/", "_")
        .replace("\\\\_", "_")
        .lower()
    )
    test_str_list.append(rev_str)

for rev in val:
    rev_str = (
        rev["review"]
        + "####"
        + str(rev["annot1"])
        .replace("#", " ")
        .replace("/", "_")
        .replace("\\\\_", "_")
        .lower()
    )
    val_str_list.append(rev_str)

train_str = "\n".join(train_str_list)
test_str = "\n".join(test_str_list)
val_str = "\n".join(val_str_list)

with open(args.output_file1, "w") as f:
    f.write(train_str)

with open(args.output_file2, "w") as f:
    f.write(test_str)

with open(args.output_file3, "w") as f:
    f.write(val_str)
