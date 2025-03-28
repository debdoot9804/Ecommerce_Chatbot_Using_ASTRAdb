from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from ecomm.ingest import ingest_data
import os

GROQ_API_KEY=os.getenv('GROQ_API_KEY')


def generate(v_store):
    retriever=v_store.as_retriever(search_kwargs={"k": 3})

    template="""
You are an Ecommerce bot, your job is to assist and guide customers with whatever queries they have regarding products and services of our platform. Your responses should be respectful and with a happy tone

CONTEXT: {context}


QUESTION : {question}

Answer:

"""

    prompt=ChatPromptTemplate.from_template(template)
    parser=StrOutputParser()

    model = ChatGroq(model_name="gemma2-9b-it")


    chain=(
        {"context": retriever,"question": RunnablePassthrough()}| prompt | model | parser
        
    )
    return chain

if __name__=='__main__':
    v_store=ingest_data("Data Already Uploaded to AstraDB")
    chain=generate(v_store)
    print(chain.invoke("Tell me some good laptops"))




