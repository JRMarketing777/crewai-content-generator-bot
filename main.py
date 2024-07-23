import os
from crewai import Crew, Process
from tasks.research_tasks import research_task
from tasks.analysis_tasks import analysis_task
from tasks.summary_tasks import summary_task
from agents.researcher import researcher
from agents.analyzer import analyzer
from agents.summarizer import summarizer
from transformers import pipeline

# Install Hugging Face Transformers if not already installed
os.system('pip install transformers')

# Set up the Hugging Face summarization model
summarizer_model = pipeline("summarization")

# Example function to summarize text using Hugging Face
def summarize_text(text):
    return summarizer_model(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

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
