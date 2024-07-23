from crewai import Task
from agents.summarizer import summarizer

summary_task = Task(
    description="""Summarize the analyzed market data into key insights.
    Provide a clear, concise summary of the selling points, niche, market, and target audience for each competitor.""",
    agent=summarizer
)
