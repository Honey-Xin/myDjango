import operator
import torch
from transformers import BertTokenizer, BertForMaskedLM
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BertTokenizer.from_pretrained("shibing624/macbert4csc-base-chinese")
model = BertForMaskedLM.from_pretrained("shibing624/macbert4csc-base-chinese")
model.to(device)

# texts = ["我的名子事你的民字，你找到你最喜欢的工作，我也很高心。儿且先在我不想去共作，我只想休息一下。"]
texts = ['谁杀了大光头：这里是无面镇，镇上的人都没有眼睛鼻子和耳朵，只有一张用来干饭的嘴。',
         '镇上有一家理发店，店长大光头的祖上也是一个剃头匠，他家里有一本祖传的“三十六路剃光妙法”，',
         '只要习得此法就能将光头将的特别的光滑白嫩，远远看去仿佛一颗几百瓦的大灯泡，',
         '不少人因此慕名而来。理发店里有个可爱漂亮的洗头小妹儿-妹妹头，还有个理发技术很牛逼总拿 ',
         '“鼻孔”看人的技师-爆炸头，哦对了，老板的堂弟-小平头也在店里学徒，就是手艺不咋地，',
         '还总色眯眯的看着洗头笑妹儿。前不久啊，店里又来了几个新人，',
         '他们分别是总在镇上闲逛的街溜子飞机头、没事就到处成']
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

def get_result():
    outputs = to_torch()

    result = []
    for ids, text in zip(outputs.logits, texts):
        _text = tokenizer.decode(torch.argmax(ids, dim=-1), skip_special_tokens=True).replace(' ', '')
        corrected_text = _text[:len(text)]
        corrected_text, details = get_errors(corrected_text, text)
        print(text, ' => ', corrected_text, details)
        result.append((corrected_text, details))
    print(result)
    return result

if __name__ == "__main__":
    get_result()