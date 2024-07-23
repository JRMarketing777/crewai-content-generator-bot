from crewai import Agent
from crewai_tools import DuckDuckGoSearchRun

researcher = Agent(
    role='Web Scraper',
    goal='Extract relevant content from the top 7 competitors',
    backstory='You are an expert web scraper with the ability to extract key information from any website.',
    verbose=True,
    allow_delegation=False,
    tools=[DuckDuckGoSearchRun()]
)
