from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.retrievers import ParentDocumentRetriever, EnsembleRetriever, MultiQueryRetriever
from langchain.storage import InMemoryStore
from langchain_community.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0)
prompt_template = """You are a helpful assistant answering all questions related to Pronto, a game mechanic prototyping framework for the Godot Game Engine. This framework introduces the concept of Behaviors. Behaviors drive the actions of game objects in a game. They can be connected to each other to create more complex interactions. Try to answer the question using the Pronto framework before thinking of using the Godot Engine. Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""
prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

query_prompt = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant for a 
    game prototyping framework called Pronto. In this framework 
    are components called Behaviors. Behaviors can be used to drive 
    game mechanics. There are many different Behaviors serving a 
    different purpose. Your task is to generate 3 different versions 
    of the given user question to retrieve relevant documents from a 
    vector database. By generating multiple perspectives on the user question, 
    your goal is to help the user overcome some of the limitations 
    of distance-based similarity search. If applicable, ask for 
    Behaviors that could help regarding the question. Provide these alternative 
    questions separated by newlines. Original question: {question}""",
)


def create_chatbot():
    docs_loader = DirectoryLoader("pronto-docs", glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    docs = docs_loader.load()

    parent_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN, chunk_size=400,
                                                                   chunk_overlap=0)
    child_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN, chunk_size=100,
                                                                  chunk_overlap=0)

    pdlg_vectorstore = Chroma(
        collection_name="split_parents",
        embedding_function=OpenAIEmbeddings(),
        persist_directory="./chroma_db"
    )
    pdlg_store = InMemoryStore()
    pdlg_retriever = ParentDocumentRetriever(
        vectorstore=pdlg_vectorstore,
        docstore=pdlg_store,
        child_splitter=child_splitter,
        parent_splitter=parent_splitter,
    )

    pdlg_retriever.add_documents(docs)

    pdlg_mq_retriever = MultiQueryRetriever.from_llm(
        retriever=pdlg_retriever, llm=llm, prompt=query_prompt
    )

    ensemble_retriever = EnsembleRetriever(
        retrievers=[pdlg_mq_retriever, pdlg_retriever], weights=[0.5, 0.5]
    )

    memory = ConversationSummaryMemory(
        llm=llm, memory_key="chat_history", return_messages=True
    )

    return ConversationalRetrievalChain.from_llm(
        llm,
        retriever=ensemble_retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt})
