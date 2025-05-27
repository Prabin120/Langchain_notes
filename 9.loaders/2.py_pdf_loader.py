from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('9.loaders\dl-curriculum.pdf')

docs = loader.load()

print(docs)