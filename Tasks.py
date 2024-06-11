from config_entity import FormAttributes
from Agents import agent_1
from crewai import Agent, Task, Crew

task_1 = Task(
    description="You are given HTML code {source_code}. Your task is to find the `id` attribute values of all input and textarea tags in the HTML code, considering the tag name value to match with the correct entity.",
    expected_output="A dictionary where keys are tag names and values are lists of input and textarea tag `id` attribute values extracted from the HTML code.",
    human_input=False,
    output_json=FormAttributes,
    output_file="form_attributes.json",
    agent=agent_1
)

