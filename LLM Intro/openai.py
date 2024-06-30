#this code is not working, might be the functin gets deprecated in latest langchain version
from langchain.llms import openAI
import os

os.environ["OPEN_API_KEY"] = ""
llm = openAI(model_name = "text-davinci-003")
our_query = "What is the currency of India?"
response = llm(our_query)
print(response)