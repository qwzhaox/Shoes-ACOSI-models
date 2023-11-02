import argparse
from json import load

ASPECT_IDX = 0
CATEGORY_IDX = 1

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help="input json file", required=True)
parser.add_argument(
    "-tr",
    "--train",
    help="output json file",
    required=True,
)
parser.add_argument(
    "-te",
    "--test",
    help="output json file",
    required=True,
)
parser.add_argument(
    "-v",
    "--val",
    help="output json file",
    required=True,
)

args = parser.parse_args()

with open(args.input_file) as f:
    review_splits = load(f)

train = review_splits["train"]
test = review_splits["test"]
val = review_splits["validation"]


def get_str_list(reviews):
    str_list = []
    for rev in reviews:
        for annot in rev["annot1"]:
            annot[CATEGORY_IDX] = (
                annot[CATEGORY_IDX].replace("#", " ").replace("/", "_")
            )
            if annot[ASPECT_IDX].lower() == "implicit":
                annot[ASPECT_IDX] = "it"
        rev_str = (
            rev["review"].lower()
            + "####"
            + str(rev["annot1"]).replace("\\\\_", "_").lower()
        )
        str_list.append(rev_str)
    return str_list


train_str_list = get_str_list(train)
test_str_list = get_str_list(test)
val_str_list = get_str_list(val)

train_str = "\n".join(train_str_list)
test_str = "\n".join(test_str_list)
val_str = "\n".join(val_str_list)

with open(args.train, "w") as f:
    f.write(train_str)

with open(args.test, "w") as f:
    f.write(test_str)

with open(args.val, "w") as f:
    f.write(val_str)
