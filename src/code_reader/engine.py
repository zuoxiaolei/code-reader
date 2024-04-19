from langchain_community.chat_models import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.globals import set_debug
from langchain.agents import create_react_agent
from langchain.agents import AgentType
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter

from prompt.desc_code_prompt import desc_code_prompt
from prompt.desc_text_prompt import desc_text_prompt
from prompt.refine_prompt import REFINE_PROMPT
from get_refine_chain import get_refine_chain
from langchain.document_loaders import UnstructuredFileLoader
import os

llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                 max_tokens=16385)

set_debug(True)


class CoderReaderWriter(object):

    def __init__(self, llm) -> None:
        self.llm = llm

    def get_file_desc(self, filename, filetype, max_chunk_size=5000):
        filename_basename = os.path.basename(filename)
        loader = UnstructuredFileLoader(filename)
        document = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=max_chunk_size,
            chunk_overlap=0
        )
        code_refine_chain = get_refine_chain(llm,
                                             desc_code_prompt.partial(filename=filename_basename),
                                             REFINE_PROMPT
                                             )
        text_refine_chain = get_refine_chain(llm,
                                             desc_text_prompt.partial(filename=filename_basename),
                                             REFINE_PROMPT)
        refine_chain = code_refine_chain if filetype == 'code' else text_refine_chain
        split_documents = text_splitter.split_documents(document)
        return refine_chain.invoke(split_documents)["output_text"]

    def get_project_desc(self, filenames):
        pass

    def optimize_project_desc(self):
        pass

    def get_code_document(self):
        pass


if __name__ == '__main__':
    crw = CoderReaderWriter(llm=llm)
    filename = "/Users/xiaoleizuo/Downloads/modeling_baichuan.py"
    print(crw.get_file_desc(filename, 'code'))
