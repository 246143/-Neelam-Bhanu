
#Importing Required Modules
from crewai import Task, Agent, Crew, Process
import crewai_tools 
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv


#Setting up the LLM Model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Setting Up Web Search Tools
from crewai_tools import SerperDevTool, WebsiteSearchTool
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


#Defining CrewAI Agents (Specialists)
manager = Agent(
        role="Kitchen Support Manager",
        goal="Identify issues and delegate to appropriate specialists.",
        backstory="Experienced kitchen maintenance coordinator with expertise in"
                  "identifying problems and efficiently delegating tasks to specialists."
                  "Known for clear communication and effective problem-solving.",
        allow_delegation=True,  # Can delegate tasks to specialists
        memory=True,             # Has memory to store information
        verbose=True,           # Provides detailed responses
        llm=llm                 # Uses the LLM model for communication
    )


carpentry_specialist= Agent(
    role="Cupboard Specialist",
            goal="Diagnose and resolve kitchen cupboard issues effectively.",
            backstory= "Expert in all aspects of kitchen cupboard maintenance and repairs,"
                      "including hinges, handles, shelving, and structural integrity."
                      "Specializes in providing practical, long-lasting solutions.",
            llm=llm,
            memory=True,
            verbose=True
)

plumbing_specialist=Agent(
            role="Water Tap Specialist",
            goal="Solve water-related issues and prevent future problems.",
            backstory="Highly experienced in diagnosing and fixing kitchen plumbing issues,"
                      "including leaks, pressure problems, and tap maintenance. Prioritizes"
                      "water conservation and efficient solutions.",
            llm=llm,
            memory=True,
            verbose=True
        )

electrical_specialist= Agent(
            role="Electrical Appliance Specialist",
            goal="Ensure safe and effective operation of kitchen electrical systems.",
            backstory="Certified expert in kitchen electrical systems and appliances."
                      "Focuses on safety-first approaches while providing effective"
                      "solutions for all electrical-related kitchen problems.",
            llm=llm,
            memory=True,
            verbose=True
        )


#Defining the Task (Kitchen Issue Handling)

kitchen_issue_task = Task(
    description=(
        "A kitchen issue has been reported: '{topic}'. "
        "As the Kitchen Support Manager, assess the problem, delegate it to the appropriate specialist, "
        "and ensure that the specialist provides a detailed report upon completion of the repair. "
        "Additionally, provide relevant web links to assist in addressing the issue."
    ),
    agent=manager,
    tools=[SerperDevTool(),WebsiteSearchTool()],
    expected_output=(
        "The manager should provide:\n"
        "- A brief assessment of the issue.\n"
        "- The specialist (agent) assigned to address it.\n"
        "- Relevant web links related to the issue.\n"
        "- Confirmation that the specialist will provide a detailed report upon completion of the repair."
    )
)
 
#Creating the Crew

crew = Crew(
    agents=[carpentry_specialist, plumbing_specialist, electrical_specialist],
    tasks=[kitchen_issue_task],
    process=Process.hierarchical,
    manager_agent=manager,
    verbose=True
)

#Running the System
result=crew.kickoff(inputs={'topic':"celling lights are not working properly sometimes blinking in my kitchen"})
print(result)