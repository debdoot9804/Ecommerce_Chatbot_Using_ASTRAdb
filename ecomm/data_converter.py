import pandas as pd
from langchain_core.documents import Document

def DataConverter():
    data=pd.read_csv("E:\\project\\data\\flipkart_product_review.csv")
    data=data[['product_title','review']]
    product_list=[]

    for index, row in data.iterrows():
        dic={
        'product_name': row['product_title'],
        'review': row['review']
        }

        product_list.append(dic)

    #Creating document
    docs=[]
    for i in product_list:
        metadata={"product_name":i['product_name']}
        doc=Document(page_content=i['review'],metadata=metadata)
        docs.append(doc)  

    return docs
      