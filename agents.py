from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## calling  the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent 

news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {query}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)


news_retriever_agent = Agent(
    role="""Retrieve relevant information to answer the user query: {query}""",
    goal="""Retrieve the most relevant information from the available sources 
             by using the web search tool.""",
    backstory="""You're a meticulous analyst with a keen eye for detail. 
                You're known for your ability understand the user query: {query} 
                and retrieve knowlege from the most suitable knowledge base.""",
    verbose=True,
    tools=[tool],
    llm=llm,
  allow_delegation=False
)
