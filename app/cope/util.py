# 文件解析模块
import docx
import fitz
# 获取word文本信息
def get_docx_text(filepath):
    # 打开Word文档
    doc = docx.Document(filepath)
    # 读取文本内容
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    text = ''.join([i.strip() for i in text.split(' ')])  # 简单处理
    return text

# 获取pdf信息
def get_pdf_text(filepath):
    doc = fitz.open(filepath)  # 打开文件
    contents = []  # 信息列表
    for i in range(doc.page_count):  # 获取信息
        page = doc.load_page(i)
        pagetext = page.get_text("text")
        contents.append(pagetext)
    text = ''.join(''.join(contents).split('\n'))
    text = ''.join([i.strip() for i in text.split(' ')])
    return text  # 返回信息