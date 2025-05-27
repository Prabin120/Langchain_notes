from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='social_ads.csv')

data = loader.load()

print(len(data))
print(data[0])