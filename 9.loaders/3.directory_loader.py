from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()  # It use to load all the pdf at once and will load in memory, which is a big problem if we have many pdf's

docs = loader.lazy_load() # it will create a generator, which won't load everything at one go. (on demand load)

# print(len(docs))

# print(docs[325].metadata)

# for document in docs:
#     print(document.metadata)