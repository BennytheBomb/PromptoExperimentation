from langchain.document_loaders import GitLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers import EnsembleRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory

from dotenv import load_dotenv
load_dotenv()


def create_chatbot():
    separators = [
        # First, try to split along class definitions
        "\nclass ",
        "\nfunc ",
        "\n\tfunc ",
        # Now split by the normal type of lines
        "\n\n",
        "\n",
        " ",
        "",
    ]

    embeddings = OpenAIEmbeddings()

    code_loader = GitLoader(
        clone_url="https://github.com/hpi-swa-lab/godot-pronto",
        repo_path="./pronto",
        branch="master",
        file_filter=lambda file_path: file_path.endswith(".gd")
    )
    code_documents = code_loader.load()

    readme_loader = UnstructuredMarkdownLoader("pronto/README.md")
    readme_document = readme_loader.load()

    code_splitter = RecursiveCharacterTextSplitter(separators=separators, chunk_size=512, chunk_overlap=200)
    code_splits = code_splitter.split_documents(code_documents)

    readme_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN, chunk_size=60,
                                                                   chunk_overlap=0)
    readme_splits = readme_splitter.split_documents(readme_document)

    code_db = Chroma.from_documents(documents=code_splits, embedding=embeddings)
    code_retriever = code_db.as_retriever(
        search_type="mmr",  # Also test "similarity"
        search_kwargs={"k": 4},
    )

    readme_db = Chroma.from_documents(documents=readme_splits, embedding=embeddings)
    readme_retriever = readme_db.as_retriever(search_kwargs={"k": 8})

    retriever = EnsembleRetriever(
        retrievers=[code_retriever, readme_retriever], weights=[0.2, 0.8]
    )

    llm = ChatOpenAI(temperature=0)
    memory = ConversationSummaryMemory(
        llm=llm, memory_key="chat_history", return_messages=True
    )
    return ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)
