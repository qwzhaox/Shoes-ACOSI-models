# from datasets import load_metric
# import pandas as pd
# import json
import argparse
from mvp_evaluate_acosi import get_mvp_output

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pkl_file", type=str, required=True)
args = parser.parse_args()

get_mvp_output(pkl_file=args.pkl_file)

# class Evaluation:
#     def __init__(self, pkl_file, process_func, data):
#         with open(pkl_file, "rb") as file:
#             self.model_output = pickle.load(file)
#         self.true_labels = [x.split("####")[1] for x in data.split(".####")]
#         self.pred_labels = self.model_output
#         self.results = self.get_results()

#     def calc_accuracy(self):
#         accuracy_metric = load_metric("accuracy")
#         return accuracy_metric.compute(
#             predictions=self.pred_labels, references=self.true_labels
#         )

#     def calc_f1_score(self):
#         F1_metric = load_metric("f1")
#         return F1_metric.compute(
#             predictions=self.pred_labels, references=self.true_labels
#         )

#     def get_results(self):
#         metrics = {
#             "accuracy": self.calc_accuracy(),
#             "f1_score": self.calc_f1_score(),
#         }
#         results = {
#             "metrics": metrics,
#             "model_output": self.model_output,
#             "true_labels": self.true_labels,
#         }
#         return json.dumps(results)
