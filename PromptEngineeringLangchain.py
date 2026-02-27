#Use this python code in jupyter notebook and run each cell.
import os
os.environ['OPENAI_API_KEY']=""
from langchain.prompts import PromptTemplate
template='i want you to act as a acting financial advisor for people.' \
'in an easy way, explain the baiscs of {financial_concept}.'
 
prompt=PromptTemplate(
    input_variables=['financial_concept'],
    template=template
)
prompt.format(financial_concept='income tax')

from langchain.llms import openai
from langchain.chains import LLMChain
llm=openai(temprature=0.6)
chain=LLMChain(llm=llm,prompt=prompt)
chain.run('income-tax')


#Language translation
from langchain.prompts import PromptTemplate
template='''In an easy way translate the following sentence '{sentence}' into '{target_language}' '''
language_prompt=PromptTemplate(
    input_variables=['sentence','target_language'],
    template=template
)
language_prompt.format(sentence='how are you',target_language='hindi')

chain2=LLMChain(llm=llm,prompt=language_prompt)
chain2.run({'sentence':'Hello how are you','target_language':'hindi'})
