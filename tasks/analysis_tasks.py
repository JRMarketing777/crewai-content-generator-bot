from crewai import Task
from agents.analyzer import analyzer

analysis_task = Task(
    description="""Analyze the extracted content to determine the market position, selling points, niche, and target audience of the top 7 competitors.
    Perform sentiment analysis to gauge the market sentiment towards each competitor.""",
    agent=analyzer
)
