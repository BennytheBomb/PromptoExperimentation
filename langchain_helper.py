from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
load_dotenv()

embeddings = OpenAIEmbeddings()


video_url = "https://www.youtube.com/watch?v=-Osca2Zax4Y"


def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db


def get_response_from_query(db, query, k=4):
    # text-davinci can handle 4097 tokens
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model="text-davinci-003")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
            You are a helpful YouTube assistant that can answer questions about videos based on the videos transcript.
            
            Answer the following question: {question}
            By searching the following video transcript: {docs}
            
            Only use the factual information from the transcript to answer the question.
            
            If you feel like you don't have enough information to answer the question, say "I don't know".
            
            Your answers should be detailed.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response


def generate_pet_names(animal_type, pet_color):
    llm = OpenAI(temperature=0.5)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )

    name = LLMChain(llm=llm, prompt=prompt_template_name,)

    response = name.run({'animal_type': animal_type, 'pet_color': pet_color})

    return response


def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

    print(result)


if __name__ == '__main__':
    print(create_vector_db_from_youtube_url(video_url))
