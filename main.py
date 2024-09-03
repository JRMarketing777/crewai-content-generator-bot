import os
import openai
from dotenv import load_dotenv
from crewai import Crew, Process
from tasks.research_tasks import research_task
from tasks.analysis_tasks import analysis_task
from tasks.summary_tasks import summary_task
from agents.researcher import researcher
from agents.analyzer import analyzer
from agents.summarizer import summarizer

# Load environment variables from .env file
load_dotenv()

# Access API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Example function to summarize text using the ChatGPT API
def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Summarize the following text:\n" + text,
        max_tokens=130,
        temperature=0.5
    )
    return response.choices[0].text

# Modify the summarizer agent to use the new summarization function
summarizer.summarize = summarize_text

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
