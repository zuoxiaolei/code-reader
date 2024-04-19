from langchain_core.prompts import PromptTemplate


REFINE_PROMPT_TMPL = """
你的任务是做一个最后的文本总结提炼.
我们已经提供了一个现有的总结，直到文档的前一部分： 
{existing_answer}

我们有机会（仅在需要时）通过下面的更多上下文来完善现有摘要。
------------
{text}
------------
在新提供增加的文本下，完善原始摘要内容，格式和原始摘要一致, 以markdown返回。
如果新增文本对完善摘要没有用处，则返回原始摘要。
"""
REFINE_PROMPT = PromptTemplate.from_template(REFINE_PROMPT_TMPL)
