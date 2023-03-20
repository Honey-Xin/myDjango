import torch
import torch.nn as nn
from transformers import BertTokenizer, BertForMaskedLM, BertModel
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载模型和分词器
model = BertModel.from_pretrained('hfl/chinese-roberta-wwm-ext')
tokenizer = BertTokenizer.from_pretrained('hfl/chinese-roberta-wwm-ext')

# 待纠正的文本
text = '今天天气很好，适合出门游玩。'

# 对文本进行分词
tokens = tokenizer.tokenize(text)

# 在每个非空格字符后插入一个"[MASK]"标记
masked_tokens = []
for token in tokens:
    if token.strip():
        masked_tokens.append("[MASK]")
    masked_tokens.append(token)
masked_tokens.append("[MASK]")

# 构造模型的输入
inputs = tokenizer.encode_plus("".join(masked_tokens), return_tensors='pt')
input_ids = inputs['input_ids']
token_type_ids = inputs['token_type_ids']
attention_mask = inputs['attention_mask']

# 使用模型进行预测
with torch.no_grad():
    outputs = model(input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask)
    predictions = outputs[0]

# 根据预测结果进行纠错
corrected_tokens = []
for i, token in enumerate(masked_tokens):
    if token == "[MASK]":
        predicted_index = torch.argmax(predictions[0, i]).item()
        predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
        corrected_tokens.append(predicted_token)
    elif token.strip():
        corrected_tokens.append(token)

# 输出纠错后的文本
corrected_text = "".join(corrected_tokens).replace(" ", "")
print(corrected_text)