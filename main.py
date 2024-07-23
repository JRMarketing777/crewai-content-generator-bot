import os
from crewai import Crew, Process
from tasks.research_tasks import research_task
from tasks.analysis_tasks import analysis_task
from tasks.summary_tasks import summary_task
from agents.researcher import researcher
from agents.analyzer import analyzer
from agents.summarizer import summarizer

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Create the Crew
crew = Crew(
    agents=[researcher, analyzer, summarizer],
    tasks=[research_task, analysis_task, summary_task],
    process=Process.sequential,
    verbose=2
)

# Run the Crew
result = crew.kickoff()
print(result)
