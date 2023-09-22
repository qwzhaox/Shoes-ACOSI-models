from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")

model = T5ForConditionalGeneration.from_pretrained("t5-base")

input_ids = tokenizer("IE", return_tensors="pt").input_ids

print(input_ids)
