from tasks import get_research_task, get_retriever_task
from agents import news_researcher, news_retriever_agent
from crewai import Crew, Process

crew = Crew(
    agents=[news_researcher, news_retriever_agent],
    tasks=[get_research_task(), get_retriever_task()],
    process=Process.sequential,
)

## starting the task execution process

result = crew.kickoff(inputs={'query': 'Machine learning vs deep learning'})
print(result)