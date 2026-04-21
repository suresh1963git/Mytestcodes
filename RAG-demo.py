import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_classic.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#Loading
PypdfFunction=PyPDFLoader('Resume.pdf')
fulltext=PypdfFunction.load()

#splitting
Mytext = '\n'.join([i.page_content for i in fulltext]) 
   
# #Splitting
text_splitter1=RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=100)
mytext1=text_splitter1.split_text(Mytext)

# #Embedding
EmbedFunction = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# #Creating vector store in FAISS DB
vectorstore = FAISS.from_texts(mytext1, EmbedFunction)
vectorstore.save_local('ResumeDB')

# #retrieving the vector store from the local directory
retriever = vectorstore.as_retriever(search_kwargs={"k": 5}) # this will give the information from the vector store 
llm=ChatOpenAI(model="gpt-4o-mini",api_key=api_key,temperature=0)
qa=RetrievalQA.from_chain_type(llm=llm,retriever=retriever) # Qa generate with the help of llm

#streamlit starts here
st.title("I am  here to Help you Friend...!")
question= st.text_input("Ask your doubts related to HR here")

#gif
gif_url = "giphy.gif"
st.image(gif_url)


if question != "quit" and question  != "":
    final_answer_dict = qa.invoke(question)
    final_answer = final_answer_dict.get("result", "No answer found.")
    lines = final_answer.split("\n") # this split the anser line by line
    lines = [line for line in lines if line.strip()!=""] #removes empty line
    bullet_text= "\n".join([f"* {line}" for line in lines]) # this will add into bullet text
   
    st.markdown(f"**Answer:** {bullet_text}")


