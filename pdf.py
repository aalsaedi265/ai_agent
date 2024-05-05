
import os
from llama_index.core import SimpleDirectoryReader, StorageContext, load_index_from_storage, VectorStoreIndex
#found on llama hub
# from llama_index.core.readers import PDFReader

#this is jack of all trades, it it does not work for you go to llama hub and you will find what yo need 
# from llama_index.core import SimpleDirectoryReader

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print(f'building index  {index_name}')
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir = index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

pdf_path = os.path.join("data", "United_States.pdf")
print(pdf_path)
usa_pdf = SimpleDirectoryReader(input_files=[pdf_path]).load_data()
usa_index = get_index(usa_pdf, "usa")
usa_engine = usa_index.as_query_engine()
