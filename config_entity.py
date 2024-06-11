from pydantic import BaseModel

class FormAttributes(BaseModel):
    firstName:str
    middleName:str
    lastName:str
    streetAddress:str
    streetAddress2:str
    city:str
    state:str
    postal:str
    email:str
    phoneNumber:str
    linkedIn:str
    writeSomeThingAboutLLM:str
    writeSomeThingAboutWebAutomation:str
    reversedLinkedList:str
    coverLetter:str