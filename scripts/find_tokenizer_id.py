from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")

model = T5ForConditionalGeneration.from_pretrained("t5-base")

input_ids = tokenizer("[I]", return_tensors="pt").input_ids

# impl_expl_tokenize_res = []

# for ie in ["direct", "indirect"]:
#     impl_expl_tokenize_res.extend(
#         tokenizer(ie, return_tensors="pt")["input_ids"].tolist()[0]
#     )

# print(tokenizer.decode(71))
print(input_ids)
