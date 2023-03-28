import operator
import torch
from transformers import BertTokenizer, BertForMaskedLM
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BertTokenizer.from_pretrained("shibing624/macbert4csc-base-chinese")
model = BertForMaskedLM.from_pretrained("shibing624/macbert4csc-base-chinese")
model.to(device)
print(model)

texts = ["我的名子事你的民字，你找到你最喜欢的工作，我也很高心。儿且先在我不想去共作，我只想休息一下。"]

# texts = []
def to_torch():
    with torch.no_grad():
        outputs = model(**tokenizer(texts, padding=True, return_tensors='pt').to(device))
        return outputs

def get_errors(corrected_text, origin_text):
    sub_details = []
    for i, ori_char in enumerate(origin_text):
        if ori_char in [' ', '“', '”', '‘', '’', '琊', '\n', '…', '—', '擤']:
            # add unk word
            corrected_text = corrected_text[:i] + ori_char + corrected_text[i:]
            continue
        if i >= len(corrected_text):
            continue
        if ori_char != corrected_text[i]:
            if ori_char.lower() == corrected_text[i]:
                # pass english upper char
                corrected_text = corrected_text[:i] + ori_char + corrected_text[i + 1:]
                continue
            sub_details.append((ori_char, corrected_text[i], i, i + 1))
    sub_details = sorted(sub_details, key=operator.itemgetter(2))
    return corrected_text, sub_details

texts = ["我的名子事你的民字，你找到你最喜欢的工作，我也很高心。儿且先在我不想去共作，我只想休息一下。"]
def get_result():
    outputs = to_torch()

    result = []
    for ids, text in zip(outputs.logits, texts):
        _text = tokenizer.decode(torch.argmax(ids, dim=-1), skip_special_tokens=True).replace(' ', '')#解码输出，转化为文字。
        corrected_text = _text[:len(text)]
        corrected_text, details = get_errors(corrected_text, text)
        print(text, ' => ', corrected_text, details)
        result.append((corrected_text, details))
    # print(result)
    return result

if __name__ == "__main__":
    get_result()
    # pass