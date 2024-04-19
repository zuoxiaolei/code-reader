from langchain_core.prompts import PromptTemplate

prompt = '''你是一个代码编程专家，你正在根据代码工程总结每个代码文件的每个重要的class或者每个function的代码实现原理和细节，使用方法。
以markdown的形式返回，格式如下：
# 代码的作用
详细解析代码的作用

# 代码的实现主要步骤
 1. 步骤1的详细说明
 2. 步骤2的详细说明
 ...(只说明主要步骤)

# 代码类定义
  （markdown表格的格式返回，只列出主要的class，每一行一个类, 列名包括 类名 类的功能含义说明 类的参数说明）


# 代码的函数定义
  （markdown表格的格式返回，只列出主要的function，每一行一个函数名称, 列名包括 函数名称 函数功能含义 函数参数说明 函数返回值说明）

# 代码的调用使用方式
   （使用代码说明和举例）
   
代码文件名称: {filename}   
代码: 
{text}
'''

desc_code_prompt = PromptTemplate.from_template(prompt)
