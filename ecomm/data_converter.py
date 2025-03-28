import pandas as pd
from langchain_core.documents import Document

def DataConverter():
    data=pd.read_csv("../data/laptops_dataset_final.csv")
    data=data[['product_name','overall_rating','review']]
    product_list=[]

    for index, i in data.iterrows():
        dic={
        'product_name': i['product_name'],
        'rating': i['overall_rating'],
        'review':i['review']

        }

        product_list.append(dic)

    #Creating document
    docs=[]
    for i in product_list:
        metadata = {"product_name": i['product_name']}
        doc = Document(page_content=f"rating: {i['rating']}\nreview:{i['review']}",metadata=metadata) 

        docs.append(doc)  

    return docs
      