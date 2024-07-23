from crewai import Agent

analyzer = Agent(
    role='Market Analyst',
    goal='Analyze the market data of the top 7 competitors',
    backstory='You are a skilled data analyst with experience in market research and sentiment analysis.',
    verbose=True,
    allow_delegation=False
)
