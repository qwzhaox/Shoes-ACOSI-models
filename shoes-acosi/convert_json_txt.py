from json import load

with open("shoes-acosi/review_splits.json") as f:
    review_splits = load(f)

train = review_splits["train"]
test = review_splits["test"]
val = review_splits["validation"]

train_str_list = []
test_str_list = []
val_str_list = []

for rev in train:
    rev_str = rev["review"] + "####" + str(rev["annot"])
    train_str_list.append(rev_str)

for rev in test:
    rev_str = rev["review"] + "####" + str(rev["annot"])
    test_str_list.append(rev_str)

for rev in val:
    rev_str = rev["review"] + "####" + str(rev["annot"])
    val_str_list.append(rev_str)

train_str = "\n".join(train_str_list)
test_str = "\n".join(test_str_list)
val_str = "\n".join(val_str_list)

with open("shoes-acosi/train.txt", "w") as f:
    f.write(train_str)

with open("shoes-acosi/test.txt", "w") as f:
    f.write(test_str)

with open("shoes-acosi/dev.txt", "w") as f:
    f.write(val_str)
