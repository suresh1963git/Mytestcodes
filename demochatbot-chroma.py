#Loading PDF and putting the text in a faiss vector database
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

PypdfFunction=PyPDFLoader('Serverdep.pdf')
fulltext=PypdfFunction.load()
Mytext = '\n'.join([i.page_content for i in fulltext]) 

#listtext=[i.page_content for i in fulltext]

#Splitting
text_splitter1=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=0)
mytext1=text_splitter1.split_text(Mytext)
#print(mytext1)
#Now embedding the text and putting it in the Chroma vector database
hugFunction = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_texts(texts=mytext1, embedding=hugFunction,persist_directory="ServerDBChorama")
vectorstore.persist() #saving the file 

#retrieving the vector store from the local directory

retriever = vectorstore.as_retriever() # this will give the retrievber from the vector store 
while True:
    query = str(input("Enter your query (or 'quit' to exit): "))
    if query.lower() == 'quit':
        break
    answer = retriever.invoke(query)
   #print(answer)
    for i in answer:
        print(i.page_content)
