from crewai import Task
from tools import tool

def get_research_task():
    from agents import news_researcher
    return Task(
        description=(
            "Identify the next big trend in {query}."
            "Focus on identifying pros and cons and the overall narrative."
            "Your final report should clearly articulate the key points,"
            "its market opportunities, and potential risks."
        ),
        expected_output='A comprehensive 4 paragraphs long report on the latest AI trends.',
        tools=[tool],
        agent=news_researcher,
    )

def get_retriever_task():
    from agents import news_retriever_agent
    return Task(
        description=(
            "Compose an insightful article on {query}."
            "Focus on the latest trends and how it's impacting the industry."
            "This article should be easy to understand, engaging, and positive."
        ),
        expected_output='A 4 to 5 paragraph article on {query} advancements formatted as markdown.',
        tools=[tool],
        agent=news_retriever_agent,
        output_file='solution.md',  # Example of output customization
        async_execution=False
    )