from langchain.chains.combine_documents.refine import RefineDocumentsChain
from langchain.chains.llm import LLMChain


def get_refine_chain(llm, question_prompt, refine_prompt,
                     document_variable_name='text',
                     initial_response_name='existing_answer',
                     verbose=True, **kwargs):
    initial_chain = LLMChain(llm=llm, prompt=question_prompt, verbose=verbose)
    refine_chain = LLMChain(llm=llm, prompt=refine_prompt, verbose=verbose)
    return RefineDocumentsChain(
        initial_llm_chain=initial_chain,
        refine_llm_chain=refine_chain,
        document_variable_name=document_variable_name,
        initial_response_name=initial_response_name,
        verbose=verbose,  # type: ignore[arg-type]
        **kwargs,
    )
