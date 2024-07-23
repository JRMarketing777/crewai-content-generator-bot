from crewai import Task
from agents.researcher import researcher

research_task = Task(
    description="""Use the DuckDuckGoSearchRun tool to search for the top 7 competitors based on the user-provided keyword and topic.
    Extract the main content, including headings, paragraphs, and any relevant metadata.
    Compile the extracted data into a structured format.""",
    agent=researcher
)
