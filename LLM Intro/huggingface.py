#install huggingface module
#pip3 install -U huggingface_hub
#pip3 install -U openai
#pip3 install -U langchain
#pip3 install -U langchain-community
#pip3 install -U langchain-huggingface
#from langchain-huggingface.llms import HuggingFaceHub
#from langchain-huggingface.llms import HuggingFaceHub
from langchain.llms import HuggingFaceHub
import os
#please uncomment below block for running the code, as the code scans are giving issue
#os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

llm = HuggingFaceHub(repo_id="google/flan-t5-large")

our_query = "what is the currency of India"
llm = llm(our_query)
print("Currency is " + llm)