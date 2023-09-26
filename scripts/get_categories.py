from ast import literal_eval


def get_acosi_categories():
    unique_categories = set()

    def add_categories(file_path):
        with open(file_path, "r") as file:
            # Iterate through each line in the file
            for line in file:
                # Split the line by '####' to separate the review text from annotations
                parts = line.split("####")
                if len(parts) == 2:
                    # Extract the annotations part and split it by ','
                    annotations = literal_eval(parts[1].strip())
                    # Iterate through each annotation and extract the category
                    for annotation in annotations:
                        category = (
                            annotation[1]
                            .strip()
                            .replace("#", " ")
                            .replace("/", "_")
                            .replace("\\_", "_")
                            .lower()
                        )
                        unique_categories.add(category)

    add_categories("multi-view-prompting/data/acosi/shoes/train.txt")
    add_categories("multi-view-prompting/data/acosi/shoes/test.txt")
    add_categories("multi-view-prompting/data/acosi/shoes/dev.txt")
    # Convert the set of unique categories to a sorted list
    category_list = sorted(list(unique_categories))
    return category_list


shoes_aspect_cate_list = get_acosi_categories()
print(shoes_aspect_cate_list)
