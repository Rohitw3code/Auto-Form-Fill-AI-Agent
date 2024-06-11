from crewai import Agent, Task, Crew
from config_entity import FormAttributes
from Agents import agent_1
from selenium import webdriver
from selenium.webdriver.common.by import By
from Tasks import task_1
import logging
from urllib import request
from bs4 import BeautifulSoup
import json

values = {
    "firstName": "Rohit",
    "middleName": "Kumar",
    "lastName": "Singh",
    "streetAddress": "vikash nagar road no 9",
    "streetAddress2": "singh more",
    "city": "Ranchi",
    "state": "Jharkhand",
    "postal": "834003",
    "email": "rohitcode005@gmail.com",
    "phoneNumber": "+9798494187",
    "linkedIn": "https://www.linkedin.com/in/rohit-kumar-66522518a/",
    "writeSomeThingAboutLLM": "LLMs are advanced AI models that can generate human-like text based on input data.",
    "writeSomeThingAboutWebAutomation": "Web automation involves using software to perform tasks on the web automatically.",
    "reversedLinkedList":"This function takes the head of a linked list as input and returns the new head of the reversed linked list. It iterates through the linked list, changing the direction of pointers to reverse the list. Finally, it returns the new head of the reversed list.",
    "coverLetter": "Dear Hiring Manager, I am excited to apply for the position at your esteemed company. My skills and experience align perfectly with the requirements of this role."
}


def run_driver():
    data = json.load(open('form_attributes.json'))
    driver = webdriver.Firefox()
    try:
        # Open the target URL
        driver.get("https://form.jotform.com/241617189501153")

        for key in data.keys():
            input_box = driver.find_element(By.ID, data[key])
            input_box.send_keys(values[key])
    except Exception as e:
        pass

url_1 = "https://form.jotform.com/241617189501153"
page = request.urlopen(url_1)
soup = BeautifulSoup(page, features="html.parser")
source_code = soup.body.prettify()

if __name__ == '__main__':
    event = Crew(
        agents=[agent_1],
        tasks=[task_1],
        verbose=True  
    )
    res = event.kickoff(inputs={'source_code': source_code, 'labels': FormAttributes})
    run_driver()
