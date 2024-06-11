from crewai import Agent, Task, Crew


agent_1 = Agent(
    role="HTML input and textarea tag ID extractor",
    goal="Extract input and textarea tag ID attributes from HTML code.",
    backstory="Specialized in parsing HTML to identify and extract input and textarea tag IDs efficiently."
)