from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import pandas as pd
import os
from ecomm.data_converter import DataConverter

load_dotenv()
ASTRA_ENDPOINT=os.getenv("ASTRA_ENDPOINT")
ASTRA_TOKEN=os.getenv("ASTRA_TOKEN")
ASTRA_KEYSPACE=os.getenv("ASTRA_KEYSPACE")


hf_embeddings = HuggingFaceEmbeddings(model_name="ibm-granite/granite-embedding-278m-multilingual")

def ingest_data(status):
    v_store=AstraDBVectorStore(
        embedding=hf_embeddings,
        collection_name="laptop_data",
        api_endpoint=ASTRA_ENDPOINT,
        token=ASTRA_TOKEN,
        namespace=ASTRA_KEYSPACE
    )

    storage=status
    
    if storage==None:
        docs=DataConverter()
        insert_ids=v_store.add_documents(docs)
    else:
        return v_store

    return v_store,insert_ids

if __name__=='__main__':
    v_store,insert_ids=ingest_data(None)
    print("\n Inserted {len(insert_ids)} documents")
    results=v_store.similarity_search("can you tell me some good laptops")

    for i in results:
        print(f" {i.page_content} ")


