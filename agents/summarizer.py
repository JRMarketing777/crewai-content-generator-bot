from crewai import Agent

summarizer = Agent(
    role='Content Summarizer',
    goal='Summarize the market research into key insights',
    backstory='You are a talented content writer with the ability to distill complex information into clear, concise summaries.',
    verbose=True,
    allow_delegation=False
)
