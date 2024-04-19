from langchain_core.prompts import PromptTemplate

prompt = '''你是一个代码编程专家，你正在根据代码工程总结每个文件的含义，使用方法。
以markdown的形式返回，格式如下：
# 文本文件的作用
详细说明文件的作用

# 文件的主要处理逻辑步骤说明
 1. 步骤1的详细说明
 2. 步骤2的详细说明
 ...(只说明主要步骤)

文件名称: {filename}
文本: 
{text}
'''

desc_text_prompt = PromptTemplate.from_template(prompt)